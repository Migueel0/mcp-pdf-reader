import asyncio
from pathlib import Path

from server.server import get_pdf_metadata, read_pdf


PDF_DIR = Path(__file__).resolve().parent / "pdfs"


def _pdf_path(name: str) -> str:
    return str(PDF_DIR / name)


def test_read_pdf_valid():
    result = asyncio.run(read_pdf(_pdf_path("simple.pdf")))
    assert result["file path"].endswith("simple.pdf")
    assert "Hello PDF" in result["extracted_text"]


def test_read_pdf_invalid_input():
    result = asyncio.run(read_pdf(""))
    assert "error" in result
    assert result["error"]["type"] == "InvalidInput"


def test_read_pdf_corrupt():
    result = asyncio.run(read_pdf(_pdf_path("corrupt.pdf")))
    assert "error" in result
    assert result["error"]["type"] == "InvalidPDF"


def test_get_pdf_metadata_valid():
    result = asyncio.run(get_pdf_metadata(_pdf_path("metadata-rich.pdf")))
    assert result["page_count"] == 1
    assert result["title"] == "Metadata Rich"
    assert result["author"] == "Test Author"


def test_get_pdf_metadata_invalid_path():
    result = asyncio.run(get_pdf_metadata("missing.pdf"))
    assert "error" in result
    assert result["error"]["type"] == "FileNotFound"
