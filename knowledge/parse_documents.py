import os
import fitz  # PyMuPDF
import docx

INPUT_DIRS = ["knowledge/sop_input/pet_safety", "knowledge/sop_input/policies"]
OUTPUT_DIR = "knowledge/parsed_text"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])

def save_text(content, filename):
    with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(content)

def process_documents():
    for input_dir in INPUT_DIRS:
        for filename in os.listdir(input_dir):
            filepath = os.path.join(input_dir, filename)
            try:
                if filename.lower().endswith(".docx"):
                    text = extract_text_from_docx(filepath)
                    save_text(text, filename.replace(".docx", ".txt"))
                elif filename.lower().endswith(".pdf"):
                    text = extract_text_from_pdf(filepath)
                    save_text(text, filename.replace(".pdf", ".txt"))
                print(f"✔ Processed: {filename}")
            except Exception as e:
                print(f"⚠️ Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_documents()
