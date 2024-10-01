import requests
from bs4 import BeautifulSoup
import argparse
import pyperclip

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

def extract_text(url, selector=None):
    response = requests.get(url)    
    soup = BeautifulSoup(response.content, 'html.parser')
        
    if selector:
        print(f"Searching for selector: {selector}")
        # Modified selector search
        selected_element = soup.find(class_=selector)
        if not selected_element:
            print("Selector not found. Here are some available classes:")
            for tag in soup.find_all(class_=True):
                print(f"- {tag.name}: {tag['class']}")
            raise ValueError(f"No element found matching selector: {selector}")
        root = selected_element
        print(f"Found element with selector: {root.name}, classes: {root.get('class')}")
    else:
        root = soup

    text = ""

    for tag in root.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'ul', 'ol']):
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
    parser.add_argument("-o", "--output", help="Output filename (if not specified, output will be copied to clipboard)")
    parser.add_argument("-s", "--selector", help="CSS selector to limit extraction scope")
    args = parser.parse_args()

    try:
        markdown_text = extract_text(args.url, args.selector)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(markdown_text)
            print(f"Conversion complete. Markdown saved to {args.output}")
        else:
            pyperclip.copy(markdown_text)
            print("Conversion complete. Markdown copied to clipboard.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()