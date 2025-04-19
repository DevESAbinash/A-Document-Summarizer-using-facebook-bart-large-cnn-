# Document Summarizer

A simple Python tool to **summarize text content from PDF and DOCX documents** using Facebook's BART model (`facebook/bart-large-cnn`) via Hugging Face Transformers. It extracts text from the document and provides a concise summary.

---

## Features

- Supports **PDF** and **DOCX** file formats
- Utilizes a **pretrained transformer model** for high-quality text summarization
- Easy to use and extend

---

## Installation

Ensure you have Python 3.7+ installed, then install the required dependencies:

```bash

pip install PyMuPDF transformers torch python-docx
```

> **Note**: `PyMuPDF` is imported as `fitz` in Python scripts.

---

## Model Used

- **Model**: [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)  
  A powerful encoder-decoder model trained specifically for summarization tasks.

---

## Usage

Run the script and provide the path to your PDF or DOCX file when prompted:

```bash
python summarizer.py
```

**Example input:**
```
Enter your path: /path/to/document.pdf
```

The script will extract the text and print the summary to the terminal.

---

## Supported Formats

- `.pdf`
- `.docx`

---

## Example Output

**Original (excerpt):**
> "Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems..."

**Summary:**
> "Artificial intelligence replicates human intelligence in machines, particularly in computer systems."

---

## Notes

- For best results, input documents should be under **1024 tokens** due to model limitations.
- The quality of the summary depends on the clarity and structure of the input text.

---

## Future Improvements

- Add support for `.txt` and other formats
- Develop a GUI or web interface
- Implement multi-language support

---

## License

This project is open-source and available under the MIT License.
```
