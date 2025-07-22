import os
import tempfile
import fitz  # PyMuPDF
import docx2txt

def extract_text_from_file(uploaded_file):
    """
    Extract text from an uploaded file (PDF or DOCX) in Django.
    :param uploaded_file: Django InMemoryUploadedFile or TemporaryUploadedFile
    :return: extracted text as a string
    """
    filename = uploaded_file.name
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        for chunk in uploaded_file.chunks():
            tmp.write(chunk)
        temp_path = tmp.name  # Get the full path of the saved file

    try:
        if ext == '.pdf':
            text = extract_text_from_pdf(temp_path)
        elif ext == '.docx':
            text = extract_text_from_docx(temp_path)
        else:
            raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")
    finally:
        # Always remove the temp file, even if an exception occurs
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return text


def extract_text_from_pdf(file_path):
    try:
        with fitz.open(file_path) as doc:
            return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        return f"Failed to extract text from PDF: {str(e)}"

def extract_text_from_docx(file_path):
    try:
        return docx2txt.process(file_path)
    except Exception as e:
        return f"Failed to extract text from DOCX: {str(e)}"
