from pypdf import PdfReader

def extract_text_from_pdf(file_path) -> str:
    """Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: Extracted text (empty string if no text found).
    """

    reader = PdfReader(file_path)

    text_chunks = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_chunks.append(page_text)

    return "\n".join(text_chunks)


