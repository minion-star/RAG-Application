# import markdown
from pypdf import PdfReader
from bs4 import BeautifulSoup
from langchain.schema import Document


# read files according to file extension
def read_file_content(file_path):
    
    if file_path.endswith('.pdf'):
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    elif file_path.endswith('.html'):
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            return soup.get_text()
    elif file_path.endswith('.md'):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()


# combine read files  
def combine_documents(md_files, pdf_files, html_files):
    
    documents = []  
    for file in md_files + pdf_files + html_files:
        content = read_file_content(file)
        doc = Document(page_content=content)
        documents.append(doc)

    return documents
