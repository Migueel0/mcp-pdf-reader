from pathlib import Path

import pytest
from pypdf.errors import PdfReadError

from tools import pdf_reader


PDF_DIR = Path(__file__).resolve().parent / "pdfs"


def _pdf_path(name: str) -> str:
    return str(PDF_DIR / name)


def test_extract_text_simple_pdf():
    text = pdf_reader.extract_text_from_pdf(_pdf_path("simple.pdf"))
    assert "Hello PDF" in text


def test_extract_text_multi_page_pdf():
    text = pdf_reader.extract_text_from_pdf(_pdf_path("multi-page.pdf"))
    assert "Page 1" in text
    assert "Page 2" in text


def test_extract_metadata_rich_pdf():
    metadata = pdf_reader.extract_metadata_from_pdf(_pdf_path("metadata-rich.pdf"))
    assert metadata["page_count"] == 1
    assert metadata["title"] == "Metadata Rich"
    assert metadata["author"] == "Test Author"


def test_extract_metadata_missing_fields():
    metadata = pdf_reader.extract_metadata_from_pdf(_pdf_path("simple.pdf"))
    assert metadata["page_count"] == 1
    assert "title" not in metadata
    assert "author" not in metadata


def test_corrupt_pdf_raises_read_error():
    with pytest.raises(PdfReadError):
        pdf_reader.extract_text_from_pdf(_pdf_path("corrupt.pdf"))
