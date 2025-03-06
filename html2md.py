import requests
from bs4 import BeautifulSoup
import argparse
import pyperclip
from markdownify import markdownify as md

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

    # Convert HTML to Markdown using markdownify
    markdown_text = md(str(root))
    return markdown_text

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