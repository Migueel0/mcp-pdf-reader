
mcp-pdf-reader
================

Lightweight MCP server that extracts text from PDFs using pypdf. Includes a small MCP service exposing a `read_pdf` tool that returns the extracted text.

Contents
- `server/` — MCP server launcher and tools used by the server.
- `tools/` — helper modules; `pdf_reader.py` contains PDF extraction logic.
- `requirements.txt` — minimal runtime dependencies.

Quick summary
- Tool: `read_pdf(file_path)` — returns a JSON-serializable dict with the original file path and the extracted text.

Requirements
- Python 3.10+ recommended
- Virtualenv (recommended)

## Installation (Windows)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install runtime dependencies with virtual environment activated:

```powershell
pip install -r requirements.txt
```

## Installation (Linux)

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install runtime dependencies with virtual environment activated

```bash
venv/bin/pip install -r requirements.txt
```

## Running the server

Recommended (runs the package as a module so imports work):

```powershell
python server\server.py
```
or on Linux/macOS:
```bash
python3 server/server.py
```

## Using the `read_pdf` tool

The MCP server exposes `read_pdf(file_path)`; how you call it depends on the MCP client. Example (local test runner):

- Run the server as shown above.
- Call the `read_pdf` tool through your MCP client with the target PDF path.

Example server response

When the `read_pdf` tool completes successfully it returns a JSON-serializable dictionary similar to:

```json
{
  "file path": "sample/path/sample_file.pdf",
  "extracted_text": "Sample text\n..."
}
```

## MCP launcher configuration

If you use a launcher that expects a JSON config, an example that runs the server using the venv Python (replace paths for your machine):

### 1. Windows
```json
{
  "mcpServers": {
    "pdf-reader": {
        "command": "PATH/TO/YOUR/VENV/Scripts/python.exe",
        "args": [
            "PATH/TO/YOUR/REPO/mcp-pdf-reader/server/server.py"
        ]
    }
  }
}
```

### 2. Linux
```json
{
  "mcpServers": {
    "pdf-reader": {
        "command": "PATH/TO/YOUR/VENV/bin/python",
        "args": [
            "PATH/TO/YOUR/REPO/mcp-pdf-reader/server/server.py"
        ]
    }
  }
}
```

---

Note: This project is an initial test-version. Future work will add more tools and improve the server's installation and deployment experience.