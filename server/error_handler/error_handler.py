import os
from typing import Dict, Any


def error_response(error_type: str, message: str) -> Dict[str, Any]:
    return {
        "error": {
            "type": error_type,
            "message": message
        }
    }


def validate_file_path(file_path: str) -> Dict[str, Any] | None:
    if not isinstance(file_path, str) or not file_path.strip():
        return error_response(
            "InvalidInput",
            "file_path must be a non-empty string pointing to a PDF file."
        )

    if not file_path.lower().endswith(".pdf"):
        return error_response(
            "InvalidInput",
            "file_path must point to a .pdf file."
        )

    if not os.path.exists(file_path):
        return error_response(
            "FileNotFound",
            "file_path does not exist."
        )

    if not os.path.isfile(file_path):
        return error_response(
            "InvalidInput",
            "file_path must point to a file, not a directory."
        )

    return None
