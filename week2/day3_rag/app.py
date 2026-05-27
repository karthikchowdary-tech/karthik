import os
import numpy as np
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

def extract_text_from_file(file_path):

    text = ""
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file_path.endswith(".txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    return text.strip()
def chunk_text(text, chunk_size=300):

    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

if __name__ == "__main__":

    file_path = input("Enter the file path: ")
    text = extract_text_from_file(file_path)
    chunks = chunk_text(text)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    print(embeddings)

    # index = faiss.IndexFlatL2(embeddings.shape[1])
    # index.add(np.array(embeddings))
    # print(f"FAISS index created with {index.ntotal} vectors.")

    print(text)