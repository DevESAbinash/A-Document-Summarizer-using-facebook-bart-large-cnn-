#pip install fitz transformers torch python-docx PyMuPDF
import torch
import fitz
import docx
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

Lmodel="facebook/bart-large-cnn"
model=AutoModelForSeq2SeqLM.from_pretrained(Lmodel)
tokenizer=AutoTokenizer.from_pretrained(Lmodel)

def Summarizer(doc_text):
    inputs=tokenizer(doc_text,return_tensors="pt",truncation=True,max_length=1024)
    summary_id=model.generate(inputs['input_ids'])
    summary=tokenizer.decode(summary_id[0],skip_special_tokens=True)
    return summary


def doc_text(path):
    if path.endswith('.pdf'):
        doc = fitz.open(path)
        text="\n".join([page.get_text() for page in doc])
        doc.close()
        return text
    elif path.endswith('.docx'):
        doc=docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return "Only pdf and docx file will support!"

path=input("Enter your path ")
text=doc_text(path)
print(Summarizer(text))