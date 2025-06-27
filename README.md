# PDF to Audiobook Converter using Python

Beginner Project - This project converts any PDF file into an audiobook using Python. It allows users to select a PDF file and reads its content aloud using a text-to-speech engine.

### Features

* Select and upload a PDF file using a file dialog
* Extracts text from each page of the PDF
* Converts the text to speech using `pyttsx3`
* Works offline (no internet required)
* Simple and lightweight script

### Technologies Used

* **Python**
* **PyPDF2** – for reading PDF files
* **pyttsx3** – for offline text-to-speech conversion
* **tkinter** – for file selection dialog

### How to Run

1. Clone this repository
2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:

   ```bash
   python main.py
   ```
4. Select any PDF file when prompted, and the content will be read aloud page by page.

### Requirements

Install the following packages (if not using `requirements.txt`):

```
pyttsx3
PyPDF2
tk
