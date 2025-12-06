# mcp-pdf-reader

MCP server that extracts text from PDF files using
**pypdf**.\
Optionally, if **Tesseract OCR** is installed, the server can also
extract text from images embedded inside PDFs.

The server exposes a single MCP tool: **`read_pdf(file_path)`**, which
returns a JSON-serializable dictionary containing the original file path
and the extracted text.

## Project Structure

-   **server/** --- MCP tool definitions used by the server
-   **tools/** --- Utility modules; `pdf_reader.py` contains PDF
    extraction logic
-   **main.py** --- MCP server launcher
-   **requirements.txt** --- Runtime dependencies

## Quick Summary

### Tool: `read_pdf(file_path)`

Returns:

``` json
{
  "file_path": "path/to/file.pdf",
  "extracted_text": "Sample extracted text..."
}
```

## Requirements

-   **Python ≥ 3.13** (recommended)
-   **virtualenv** (recommended)
-   **Tesseract OCR** (optional, required only for OCR on images inside
    PDFs)

## Installing Dependencies (Windows)

1.  Create and activate a virtual environment:

``` powershell
python -m venv venv
.venv\Scripts\activate
```

2.  Verify your Python version:

``` powershell
python --version
```

3.  Install dependencies:

``` powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Installing Dependencies (Linux)

1.  Create and activate a virtual environment:

``` bash
python3 -m venv venv
source venv/bin/activate
```

2.  Verify your Python version:

``` bash
python3 --version
```

3.  Install dependencies:

``` bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

## Installing Tesseract (Optional)

Follow the official installation instructions:\
https://tesseract-ocr.github.io/tessdoc/Installation.html

You may need to manually add `tesseract` to your system `PATH`.

More details available in the Tesseract User Manual:\
https://github.com/tesseract-ocr/tessdoc

## Configuring Environment Variables

Rename `env.example` to `.env` and set your Tesseract binary path.

Example:

``` txt
# Windows
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe

# Linux
TESSERACT_CMD=/usr/bin/tesseract
```

## Running the Server

Launch the MCP server using:

``` bash
python main.py
```

If everything is configured correctly, the server will start and expose
the `read_pdf` tool.

## MCP Usage Example

Call the tool from your MCP client:

### Tool exposed:

    read_pdf(file_path)

### Example response:

``` json
{
  "file_path": "sample/path/sample_file.pdf",
  "extracted_text": "Sample text
..."
}
```

## MCP Launcher Configuration

### Windows

``` json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "PATH/TO/VENV/Scripts/python.exe",
      "args": [
        "PATH/TO/REPO/mcp-pdf-reader/main.py"
      ]
    }
  }
}
```

### Linux

``` json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "PATH/TO/VENV/bin/python",
      "args": [
        "PATH/TO/REPO/mcp-pdf-reader/main.py"
      ]
    }
  }
}
```

## Notes

This project is an early test version. Future updates will extend
available tools and improve installation and deployment workflows.
