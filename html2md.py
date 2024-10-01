import requests
from bs4 import BeautifulSoup
import argparse

def process_inline_elements(element):
    result = ""
    for child in element.children:
        if child.name == 'code':
            result += f"`{child.get_text(strip=True)}`"
        elif child.string:
            result += child.string
    return result.strip()

def process_list(list_tag, indent=0):
    list_type = 'ol' if list_tag.name == 'ol' else 'ul'
    result = ""
    for index, item in enumerate(list_tag.find_all('li', recursive=False)):
        prefix = f"{index + 1}. " if list_type == 'ol' else "- "
        content = process_inline_elements(item)
        result += f"{'  ' * indent}{prefix}{content}\n"
        
        # Handle nested lists
        nested_list = item.find(['ul', 'ol'])
        if nested_list:
            result += process_list(nested_list, indent + 1)
    
    return result

def extract_block_code(code_element):
    return code_element.get_text(strip=True)

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text = ""

    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'ul', 'ol']):
        if tag.name.startswith('h'):
            text += f"{'#' * int(tag.name[1])} {tag.get_text(strip=True)}\n\n"
        elif tag.name == 'p':
            text += f"{process_inline_elements(tag)}\n\n"
        elif tag.name == 'pre':
            code_element = tag.find('code')
            if code_element:
                code_content = extract_block_code(code_element)
                text += f"```\n{code_content}\n```\n\n"
            else:
                text += f"{tag.get_text(strip=True)}\n\n"
        elif tag.name in ['ul', 'ol']:
            text += process_list(tag) + "\n"
    
    return text

def main():
    parser = argparse.ArgumentParser(description="Convert HTML to Markdown")
    parser.add_argument("url", help="URL of the HTML page to convert")
    parser.add_argument("-o", "--output", default="output.md", help="Output filename (default: output.md)")
    args = parser.parse_args()

    markdown_text = extract_text(args.url)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    print(f"Conversion complete. Markdown saved to {args.output}")

if __name__ == "__main__":
    main()