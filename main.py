import pyttsx3                             # imports pyttsx3 library — it's used to convert text to speech (text-to-audio output)
import PyPDF2                              # imports PyPDF2, a library used to read and extract content from PDF files

from tkinter.filedialog import *           # imports file dialog box from Tkinter, so that a user can browse and select a PDF file 

Name = askopenfilename()                   # opens a file selection dialog and stores path of selected PDF in variable Name
ReadPdf = PyPDF2.PdfReader(Name)           # opens selected PDF file and loads it so it can be read
pages = len(ReadPdf.pages)                 # counts total number of pages in PDF and stores it in variable pages

for num in range(pages):                   # starts a loop from 0 to last page, so that we can read one page at a time
    page = ReadPdf.pages[num]              # line gets current page using page number in loop
    text = page.extract_text()             # extracts text content from current page
    if text:                               # checks ifre is any text on page
        print(text)                        # prints extracted text to console
        
     
    engine = pyttsx3.init()                # initializes the text-to-speech engine
    
    engine.setProperty('rate', 150)        #Sets speed of speech (150 words per minute is a normal pace
    engine.setProperty('volume', 1)        #Sets volume of speech (1.0 is maximum volume)
    
    engine.say(text)                       # converts extracted text into speech, so computer can read it aloud
    engine.runAndWait()                    # waits for speech to finish before moving on to next page

