# HTML to Markdown Converter

This Python script converts HTML content from a web page to Markdown format. It's particularly useful for extracting specific content from web pages using CSS selectors.

## Features

- Converts HTML to Markdown
- Supports extracting content from a specific HTML element using CSS selectors
- Handles headings, paragraphs, lists (ordered and unordered), and code blocks
- Preserves inline code formatting

## Requirements

- uv (Universal Versioning Tool)

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

### One-time use (without installation)

```bash
uvx html2md https://example.com -s main-content -o output.md
```

### Install the tool

```bash
uv tool install html2md
```

After installation, you can use the tool directly:

```bash
html2md https://example.com -s main-content -o output.md
```

### Upgrade the tool

```bash
uv tool upgrade html2md
```

## Options

- `url`: The web page URL to convert (required)
- `-o`, `--output`: Output filename (default: output.md)
- `-s`, `--selector`: CSS selector to limit extraction scope

## Examples

Convert an entire page:
```bash
html2md https://example.com
```

Extract content from a specific class:
```bash
html2md https://example.com -s main-content
```

Specify an output file:
```bash
html2md https://example.com -o my_output.md
```

## Limitations

- Does not handle JavaScript-rendered content
- Limited support for complex HTML structures
- May not preserve all formatting from the original HTML

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
