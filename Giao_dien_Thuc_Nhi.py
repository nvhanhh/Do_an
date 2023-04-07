from tkinter import *
from PIL import ImageTk, Image


#Khởi tạo trang đầu tiên
trang1 = Tk()
trang1.title('V4U')
trang1.geometry('1440x1024')
trang1['bg'] = '#CCFFCC'

#Chủ đề con người
#Tạo dòng chữ theo chủ đề
chu_de1 = Label(trang1, text = 'Chủ đề con người ', font = ('Times new roman',15),
                fg = '#000000', bg = '#CCFFCC')
chu_de1.place(x = 50, y = 30 )

#Tạo nút xem thêm
name_1 = Button(trang1, text = '>>', font = ('Times new roman',10),
                bg = '#CCFFFF', height = 5, width = 7)
name_1.place(x = 1200, y = 80)

#Tạo các bìa sách
#Nhaf giả kim
def click_nhagiakim():
    nd1 = Tk()
    nd1.title('V4U')
    nd1.geometry('1440x1024')
    nd1['bg'] = '#CCFFCC'

    nd1_1 = Label (nd1, text = 'Nhà Giả Kim - Paulo Coelho', font = ('Times new romman',19),
                   fg = '#000000', bg = '#CCFFCC')
    nd1_1.place(x = 50, y = 50)
    nd1_2 = Label (nd1, text = 'Truyện Nhà Giả Kim của tác giả Paulo Coelho là một truyện hot trong tháng, khi người nào muốn điều gì thì cả vũ trụ sẽ chung sức lại để người ấy đạt được điều mơ ước.\nNhững thứ vào miệng con người không độc hại, xấu xa. Xấu xa, độc hại là những gì từ miệng họ tuôn ra. Nếu cậu hiểu rõ trái tim mình thì sẽ không xảy ra\n điều gì bất trắc đâu, vì cậu biết rõ nó mơ ước gì và biết phải ứng xử như thế nào.Không ai trốn tránh được trái tim mình thành ra \nnên lắng nghe nó nói là hay hơn cả. Như thế cậu sẽ không bao giờ bị đánh bất ngờ.',
                   font = ('Times new romman',13), fg = '#000000', bg = '#CCFFCC')
    nd1_2.place(x = 50, y = 100)

img_import = (Image.open(r'D:\sách V4U\con người\nha-gia-kim.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img, command = click_nhagiakim)
sach_1.place(x = 50, y = 70)

#Đắc nhân tâm
def click_dacnhantam():
    nd2 = Tk()
    nd2.title('V4U')
    nd2.geometry('1440x1024')
    nd2['bg'] = '#CCFFCC'

    nd2_1 = Label(nd2, text='Đắc Nhân Tâm - Dale Carnegie', font=('Times new romman', 19),
                  fg='#000000', bg='#CCFFCC')
    nd2_1.place(x=50, y=50)
    nd2_2 = Label(nd2, text='Không còn nữa khái niệm giới hạn, Đắc Nhân Tâm là nghệ thuật thu phục lòng người, là làm cho tất cả mọi người yêu mến mình. Đắc nhân tâm và cái Tài trong mỗi\n người chúng ta. Đắc Nhân Tâm trong ý nghĩa đó cần được thụ đắc bằng sự hiểu rõ bản thân, thành thật với chính mình, hiểu biết và quan tâm đến những người\n xung quanh để nhìn ra và khơi gợi những tiềm năng ẩn khuất nơi họ, giúp họ phát triển lên một tầm cao mới. Đây chính là nghệ thuật cao nhất về con người\n và chính là ý nghĩa sâu sắc nhất đúc kết từ những nguyên tắc vàng của Dale Carnegie. Quyển sách Đắc nhắn tâm là cuốn sách “đầu tiên và hay nhất mọi \nthời đại về nghệ thuật giao tiếp và ứng xử”, quyển sách đã từng mang đến thành công và hạnh phúc cho hàng triệu người trên khắp thế giới.',
                  font=('Times new romman', 13), fg='#000000', bg='#CCFFCC')
    nd2_2.place(x=70, y=100)

img_import = (Image.open(r'D:\sách V4U\con người\dac-nhan-tam.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img1 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img1, command = click_dacnhantam)
sach_1.place(x = 250, y = 70)
#babylon
img_import = (Image.open(r'D:\sách V4U\con người\babylon.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img2 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img2)
sach_1.place(x = 450, y = 70)
#Đọc vị bất k ai
img_import = (Image.open(r'D:\sách V4U\con người\doc-vi-bat-ky-ai.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img3 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img3)
sach_1.place(x = 650, y = 70)
#Ranh giới 5%
img_import = (Image.open(r'D:\sách V4U\con người\ranh_gioi_5.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img4 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img4)
sach_1.place(x = 850, y = 70)
#Trí tuệ Do Thái
img_import = (Image.open(r'D:\sách V4U\con người\tri-tue-do-thai.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img5 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img5)
sach_1.place(x = 1050, y = 70)

#tên sách nhà giả kim
nha_gia_kim = Label(trang1, text = 'Nhà giả kim \n(Paulo Coelho)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
nha_gia_kim.place(x = 50, y = 180 )

#tên sách đắc nhân tâm
dac_nhan_tam = Label(trang1, text = 'Đắc Nhân Tâm \n(Dale Carnegie)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
dac_nhan_tam.place(x = 250, y = 180 )

#tên babylon
babylon = Label(trang1, text = 'Người giàu nhất... \n(George Samuel Clason)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
babylon.place(x = 420, y = 180 )

#tên đọc vị bất kỳ ai
doc_vi = Label(trang1, text = 'Đọc vị bất kỳ ai \n(George Samuel Clason)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
doc_vi.place(x = 620, y = 180 )

#tên Ranh giới 5%
ranh_gioi = Label(trang1, text = 'Ranh giới 5% \n(Michael Alden)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
ranh_gioi.place(x = 850, y = 180 )

#tên Trí tệ Do Thái
do_thai = Label(trang1, text = 'Trí tuệ Do Thái \n(Eran Katz)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
do_thai.place(x = 1050, y = 180 )







#Chủ đề kinh doanh
#Tạo dòng chữ theo chủ đề
chu_de2 = Label(trang1, text = 'Chủ đề kinh doanh ', font = ('Times new roman',15),
                fg = '#000000', bg = '#CCFFCC')
chu_de2.place(x = 50, y = 260 )

#Tạo nút xem thêm
name_2 = Button(trang1, text = '>>', font = ('Times new roman',10),
                bg = '#CCFFFF', height = 5, width = 7)
name_2.place(x = 1200, y = 310)

#Tạo các bìa sách
#Bí quyết đầu tư
img_import = (Image.open(r'D:\Sách V4U\Kinh doanh\bi-quyet-dau-tu.JPEG'))
size = img_import.resize((100,100), Image.LANCZOS)
img6 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img6)
sach_1.place(x = 50, y = 300)
#Nghĩ lớn làm lớn
img_import = (Image.open(r'D:\Sách V4U\Kinh doanh\nghi-lon-lam-lon.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img7 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img7)
sach_1.place(x = 250, y = 300)
#Những người khổng lồ
img_import = (Image.open(r'D:\Sách V4U\Kinh doanh\khong-lo.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img8 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img8)
sach_1.place(x = 450, y = 300)
#Quốc gia khởi nghiệp
img_import = (Image.open(r'D:\Sách V4U\Kinh doanh\quoc-gia-khoi-nghiep.png'))
size = img_import.resize((100,100), Image.LANCZOS)
img9 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img9)
sach_1.place(x = 650, y = 300)
#Con đường đi đến thành công
img_import = (Image.open(r'D:\Sách V4U\Kinh doanh\thanh-cong.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img10 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img10)
sach_1.place(x = 850, y = 300)
#Thịnh vượng tài chính tuổi 30
img_import = (Image.open(r'D:\Sách V4U\Kinh doanh\thinh-vuong.JPG'))
size = img_import.resize((100,100), Image.LANCZOS)
img11 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img11)
sach_1.place(x = 1050, y = 300)

#tên sách Bí quyết đầu tư
bi_quyet = Label(trang1, text = 'Bí quyết đầu tư...\n(Mark Tier)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
bi_quyet.place(x = 50, y = 410 )

#tên Nghĩ lớn làm lớn
nghi_lon = Label(trang1, text = 'Dám nghĩ lớn \n(David J. Schwartz)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
nghi_lon.place(x = 240, y = 410 )

#tên Nhưững người khổng lồ trong giới kinh doanh
babylon = Label(trang1, text = 'Người khổng lồ ... \n(Richard S.Tedlow)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
babylon.place(x = 440, y = 410 )

#tên đọc vị bất kỳ ai
khoi_nghiep = Label(trang1, text = 'Quốc gia khởi nghiệp\n(Trung Nguyên)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
khoi_nghiep.place(x = 630, y = 410 )

#tên Con đường đi đến thành công bằng sự tử tế
thanh_cong = Label(trang1, text = 'Con đường đi đến...\n(Inamori Kazuo)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
thanh_cong.place(x = 835, y = 410 )

#tên sách Thịnh vượng tài chính ở tuổi 30
thinh_vuong = Label(trang1, text = 'Thịnh vượng tài...\n(Nhiều tác giả)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
thinh_vuong.place(x = 1040, y = 410 )






#Chủ đề ngoại ngữ
#Tạo dòng chữ theo chủ đề
chu_de3 = Label(trang1, text = 'Chủ đề ngoại ngữ ', font = ('Times new roman',15),
                fg = '#000000', bg = '#CCFFCC')
chu_de3.place(x = 50, y = 500 )

#Tạo nút xem thêm
name_3 = Button(trang1, text = '>>', font = ('Times new roman',10),
                bg = '#CCFFFF', height = 5, width = 7)
name_3.place(x = 1200, y = 550)

#Tạo các bìa sách
#Hary Potter
img_import = (Image.open(r'D:\Sách V4U\Ngoại ngữ\harrypotter.jpg'))
size = img_import.resize((100,100), Image.LANCZOS)
img12 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img12)
sach_1.place(x = 50, y = 540)
#Thankful
img_import = (Image.open(r'D:\Sách V4U\Ngoại ngữ\thankful.jpg'))
size = img_import.resize((100,100), Image.LANCZOS)
img13 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img13)
sach_1.place(x = 250, y = 540)
#Theory and practice...
img_import = (Image.open(r'D:\Sách V4U\Ngoại ngữ\Theory.jpg'))
size = img_import.resize((100,100), Image.LANCZOS)
img14 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img14)
sach_1.place(x = 450, y = 540)
#Theory of Ivolutionary
img_import = (Image.open(r'D:\Sách V4U\Ngoại ngữ\Theory-of-Evolutionary.jpg'))
size = img_import.resize((100,100), Image.LANCZOS)
img15 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img15)
sach_1.place(x = 650, y = 540)
#Theory of information
img_import = (Image.open(r'D:\Sách V4U\Ngoại ngữ\Theory-of-inf.jpg'))
size = img_import.resize((100,100), Image.LANCZOS)
img16 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img16)
sach_1.place(x = 850, y = 540)
#Who's in your room
img_import = (Image.open(r'D:\Sách V4U\Ngoại ngữ\who.jpg'))
size = img_import.resize((100,100), Image.LANCZOS)
img17 = ImageTk.PhotoImage(size)
sach_1 = Button (trang1, text = ' ', image = img17)
sach_1.place(x = 1050, y = 540)

#tên Hary Potter
harry = Label(trang1, text = 'Harry Potter\n(J. K. Rowling)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
harry.place(x = 50, y = 650 )

#tên The way to be Thankful
thankful = Label(trang1, text = 'The way to be Thankful\n(The Wanderers)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
thankful.place(x = 220, y = 650 )

#Tên Theory and practice...
theory1 = Label(trang1, text = 'Theory and Practice in...\n(Lorna Tilley)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
theory1.place(x = 420, y = 650 )

#tên Theory of Ivolutionary
theory2 = Label(trang1, text = 'Theory of Evolutionary...\n(Benjamin Doerr)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
theory2.place(x = 620, y = 650 )

#tên Theory of information
theory3 = Label(trang1, text = 'Theory of information...\n(Ruslan L. Stratonovich)', font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
theory3.place(x = 820, y = 650 )

#tên Who's in your room?
who = Label(trang1, text = "Who's in your room?\n(Stewart Emery)", font = ('Times new roman',13),
                fg = '#000000', bg = '#CCFFCC')
who.place(x = 1030, y = 650 )


trang1.mainloop()