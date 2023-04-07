import pyttsx3
from PyPDF2 import *

blviet = [["Cuộc chiến Disney", "DW.pdf"], ["Những người khổng lồ trong giới kinh doanh", "NKLGKD.pdf"]]
bleng = [["Theory and Practice in the Bioarchaeology of Care", "TaPBoC.pdf"], ["Theory of Evolutionary Computation", "ToEC.pdf"], ["Theory of Information and its Value", "ToIaV.pdf"]]
speedrate = [["Nhanh", "300"], ["Chuẩn", "200"], ["Chậm", "100"]]

bot = pyttsx3.init()
voices = bot.getProperty("voices")

print("Danh sách ID giọng hiện có:")
for voice in voices:
       print (f"{voice.name}")
a = int(input("Chọn ID giọng (theo thứ tự): "))
bot.setProperty("voice", voices[a-1].id)

print("Danh sách tốc độ đọc hiện có:")
for i in range (speedrate.__len__()):
   print("\t"+ speedrate[i][0])
speed = input("Chọn tốc độ đọc mong muốn: ")
for i in range (speedrate.__len__()):
   if speed == speedrate[i][0]:
       spd = speedrate[i][1]
       bot.setProperty("rate", spd)

print("Danh sách audiobook hiện có:")
print ("\tAudiobook tiếng việt [Mã: 10]:")
for i in range (blviet.__len__()):
   print("\t\t"+ blviet[i][0])
print ("\tAudiobook tiếng anh [Mã: 20]:")
for i in range (bleng.__len__()):
   print("\t\t"+ bleng[i][0])

b = int(input("Nhập mã danh sách audiobook: "))
m = input("Nhập tên sách: ")
def choose_book():
   if b == 10:
       d = blviet.__len__()
       for i in range (d):
           if m == blviet[i][0]:
               c = blviet[i][1]
   elif b == 20:
       d = bleng.__len__()
       for i in range(d):
           if m == bleng[i][0]:
               c = bleng[i][1]
   return c

c = choose_book()
book = open(c, "rb")
reader = PdfReader(book)
nums = len(reader.pages)
pg = int(input("Nhập trang bạn muốn bắt đầu đọc: "))
current_page = pg - 1
while current_page < nums:
   page = reader.pages[current_page]
   text = page.extract_text()
   bot.say(text)
   bot.runAndWait()
   stp = int(input("Muốn dừng đọc thì nhấn số 0: "))
   if stp == 0 or current_page == nums:
       bot.stop()
       break
   else:
       current_page += 1
