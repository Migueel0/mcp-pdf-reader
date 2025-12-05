import io
from PIL import Image
import pytesseract
from pypdf import PdfReader

pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"


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

        for image_file_object in page.images:
            try:
                image = Image.open(io.BytesIO(image_file_object.data))
                ocr_text = pytesseract.image_to_string(image)
                if ocr_text:
                    text_chunks.append(ocr_text)
            except Exception:
                continue

    return "\n".join(text_chunks)
