```markdown
# Document Summarizer

This is a simple Python tool to **summarize text content from PDF and DOCX documents** using Facebook's BART model (`facebook/bart-large-cnn`) from Hugging Face Transformers. It extracts text from the document and provides a concise summary.

## Features

- Supports **PDF** and **DOCX** file formats.
- Uses a **pretrained transformer model** for high-quality text summarization.
- Easy to use and extend.

---

## Installation

Make sure you have Python 3.7+ installed, then install the required dependencies:

```bash
```
pip install fitz PyMuPDF transformers torch python-docx
```

---

## Model Used

- **Model**: [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)  
  A powerful encoder-decoder model trained for summarization tasks.

---

## Usage

Run the script and provide the path to your PDF or DOCX file when prompted:

```bash
python summarizer.py
```

Example:
```
Enter your path: /path/to/document.pdf
```

The script will extract the text and output a summary to the terminal.

---

## Supported Formats

- `.pdf`
- `.docx`

---

## Example

If you input a DOCX or PDF document with lengthy paragraphs, the script will output something like:

**Original (excerpt):**
> "Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems..."

**Summary:**
> "Artificial intelligence replicates human intelligence in machines, particularly in computer systems."

---

##  Notes

- The input document should be under **1024 tokens** for best results due to model constraints.
- Summarization quality depends on the clarity and structure of the input text.

---

## Future Improvements

- Add support for `.txt` or other formats.
- GUI or web interface for easier interaction.
- Multi-language support.

---

## License
This project is open-source and available under the MIT License.
