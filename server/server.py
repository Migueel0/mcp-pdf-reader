from typing import Dict, Any
from mcp.server import FastMCP
from tools import pdf_reader

server = FastMCP("pdf-reader")


@server.tool("read_pdf", description="Extracts text from a PDF file.")
async def read_pdf(file_path: str) -> Dict[str, Any]:
    """Reads and extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file."""

    text = pdf_reader.extract_text_from_pdf(file_path)
    return {
        "file path": file_path,
        "extracted_text": text
    }

@server.tool("get_pdf_metadata")
async def get_pdf_metadata(file_path:str) -> Dict[str,Any]:
    """Extracts metadata from a PDF file.

    Args:
        file_path (str): The path to the PDF file."""
    
    return pdf_reader.extract_metadata_from_pdf(file_path)



def run():
    server.run()
