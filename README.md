# HTML to Markdown Converter

This Python script converts HTML content from a web page to Markdown format. It's particularly useful for extracting specific content from web pages using CSS selectors.

## Features

- Converts HTML to Markdown
- Supports extracting content from a specific HTML element using CSS selectors
- Handles headings, paragraphs, lists (ordered and unordered), and code blocks
- Preserves inline code formatting

## Requirements

- Python 3.6+
- BeautifulSoup4
- Requests

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/html-to-markdown.git
   cd html-to-markdown
   ```

2. Install `uv` if you don't have it:
   ```
   curl -sSL https://install.astral.sh | bash
   ```

## Usage

Basic usage:
```
uv run python html2md.py <URL> [-o <output_file>] [-s <CSS_selector>]
```

- `<URL>`: The URL of the web page to convert.
- `-o <output_file>`: (Optional) The output Markdown file name. Default is `output.md`.
- `-s <CSS_selector>`: (Optional) CSS selector to limit extraction scope.

Example:
```
uv run python html2md.py https://example.com/page/ -o example.md -s main-content
```

This command will convert the HTML content from `https://example.com/page/` and save it to `example.md`, only extracting content from the element with the CSS class `main-content`.

This will convert the content within the element with class "main-content" from https://example.com/page/ and save it as example.md.

## Alias for Easy Use

For easier use, you can create an alias in your shell configuration file (e.g., .bashrc, .zshrc):

```
alias html2md="python /path/to/html2md.py"
```

Then you can use it like this:

```
html2md https://example.com/page/ -s content-class
```

## Limitations

- Does not handle JavaScript-rendered content
- Limited support for complex HTML structures
- May not preserve all formatting from the original HTML

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
