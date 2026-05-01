import logging
from typing import Dict, Any
from mcp.server import FastMCP
from pypdf.errors import PdfReadError
from tools import pdf_reader
from server.error_handler.error_handler import validate_file_path, error_response

server = FastMCP("pdf-reader")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@server.tool("read_pdf", description="Extracts text from a PDF file.")
async def read_pdf(file_path: str) -> Dict[str, Any]:
    """Reads and extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file."""

    validation_error = validate_file_path(file_path)
    if validation_error:
        return validation_error

    try:
        text = pdf_reader.extract_text_from_pdf(file_path)
        return {
            "file path": file_path,
            "extracted_text": text
        }
    except PdfReadError:
        logger.exception("Failed to parse PDF: %s", file_path)
        return error_response(
            "InvalidPDF",
            "PDF file could not be parsed. The file may be corrupt or unsupported.")
    except Exception as exc:
        logger.exception(
            "Unexpected error extracting text from: %s",
            file_path)
        return error_response("ProcessingError", str(exc))


@server.tool("get_pdf_metadata")
async def get_pdf_metadata(file_path: str) -> Dict[str, Any]:
    """Extracts metadata from a PDF file.

    Args:
        file_path (str): The path to the PDF file."""

    validation_error = validate_file_path(file_path)
    if validation_error:
        return validation_error

    try:
        return pdf_reader.extract_metadata_from_pdf(file_path)
    except PdfReadError:
        logger.exception("Failed to parse PDF: %s", file_path)
        return error_response(
            "InvalidPDF",
            "PDF file could not be parsed. The file may be corrupt or unsupported.")
    except Exception as exc:
        logger.exception(
            "Unexpected error extracting metadata from: %s",
            file_path)
        return error_response("ProcessingError", str(exc))


def run():
    server.run()
