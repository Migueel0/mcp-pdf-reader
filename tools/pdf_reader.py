import io
import os
from PIL import Image
import pytesseract
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = \
    os.getenv("TESSERACT_CMD")


def extract_text_from_pdf(file_path) -> str:
    """Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: Extracted text (empty string if no text found).
    """

    reader = PdfReader(file_path)

    pages = []
    for page in reader.pages:
        page_text = page.extract_text()

        for image_file_object in page.images:
            try:
                image = Image.open(io.BytesIO(image_file_object.data))
                ocr_text = pytesseract.image_to_string(image)
                if ocr_text:
                    page_text += ocr_text
            except Exception:
                continue

        if page_text:
            pages.append(page_text)

    full_text = "\n".join(pages)
    return full_text
