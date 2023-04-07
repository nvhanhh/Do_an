import pyttsx3
#from pikepdf import Pdf
from pypdf import PdfReader

#docinfo = pdf.docinfo
#for key, value in docinfo.items():
    #print(key, ":", value)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

pdf = PdfReader("anne-of-green-gables.pdf")
nums = len(pdf.pages)
print(nums)
for i in range(0, nums):
    page = pdf.pages[i]
    text = page.extract_text()
    engine.say(text)
    print(text)
    engine.runAndWait()











