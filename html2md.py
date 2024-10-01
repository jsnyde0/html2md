import requests
from bs4 import BeautifulSoup
import argparse

def extract_code_block(code_element):
    # Extract text from code block, including nested span and p elements
    code_text = ""
    for element in code_element.contents:
        if element.name in ['span', 'p'] or element.string:
            code_text += element.get_text(strip=True) + "\n"
    return code_text.strip()

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text = ""

    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'code']):
        if tag.name.startswith('h'):
            text += f"{'#' * int(tag.name[1])} {tag.get_text(strip=True)}\n\n"
        elif tag.name == 'code':
            code_content = extract_code_block(tag)
            text += f"```\n{code_content}\n```\n\n"
        else:
            text += f"{tag.get_text(strip=True)}\n\n"
    
    return text

def save_to_markdown(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    parser = argparse.ArgumentParser(description="Extract text from a webpage and save it as Markdown.")
    parser.add_argument("url", help="URL of the webpage to extract text from")
    parser.add_argument("-o", "--output", default="output.md", help="Output filename (default: output.md)")
    args = parser.parse_args()

    extracted_text = extract_text(args.url)
    save_to_markdown(extracted_text, args.output)
    print(f"Text extracted and saved to {args.output}")

if __name__ == "__main__":
    main()