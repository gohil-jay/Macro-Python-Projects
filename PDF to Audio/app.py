import pyttsx3, PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('pdf_file.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfReader.numpages):
  text = pdfReader.getPage(page_num).extractText()
  speaker.say(text)
  speaker.runAndWait()

speaker.stop()
