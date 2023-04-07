import pyttsx3
from PyPDF2 import PdfReader


n = int(input())
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')


if n == 0:
    reader = PdfReader('Thelittleprince.pdf')
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 130)
    engine.setProperty('volume', 2)
    for i in range(0, number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        engine.say(text)
        engine.runAndWait()
elif n == 1:
    reader = PdfReader('Toi Thay Hoa Vang Tren Co Xanh.pdf')
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    vivoice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
    engine.setProperty("voice", vivoice)
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 3)
    for i in range(0, number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        engine.say(text)
        engine.runAndWait()


