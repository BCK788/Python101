from tkinter import *
from tkinter import ttk #ธีม
from tkinter import messagebox
from PIL import Image, ImageTk
######
import csv

def writecsv(datalist):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)


def readcsv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

data = readcsv()
print(data)

########


GUI = Tk () #จอหลัก
GUI.title ('จะไปอยู่บ้านไหน') #ชื่อโปรแกรม
GUI.geometry('1000x500') #ขนาด


hat=PhotoImage(file="GUI--TK/NEW/file.png")
lh=Label(GUI,image=hat)
lh.pack()

#กรอกชื่อ
v_name = StringVar() # ตัวแปลพิเศษที่ใช้กับ GUI
LF1 = ttk.LabelFrame(GUI,text='ท่านชื่ออะไร')
LF1.pack()

E1 = ttk.Entry(LF1,textvariable=v_name)
E1.pack(padx=10,pady=10)

#คำถาม

question = Label(GUI, text="ดึกดื่นเมื่อเดินไปตามถนนเพียงลำพัง คุณได้ยินเสียงร้องแปลกๆ คุณจะทำอย่างไร" ,fg='blue')
question.pack()

var = IntVar()

option1 = Radiobutton(GUI, text="เดินด้วยความระมัดระวัง โดยถือไม้กายสิทธิ์และมองหาสิ่งรบกวน", variable=var, value=1)
option1.pack()

option2 = Radiobutton(GUI, text="ถอยเข้าไปในเงามืดเพื่อรอว่ามีอะไร ในขณะนั้นคุณก็ทบทวนคาถาป้องกันและโจมตีที่เหมาะสม", variable=var, value=2)
option2.pack()

option3 = Radiobutton(GUI, text="วาดไม้กายสิทธิ์และหยุดยืนอยู่กับที่", variable=var, value=3)
option3.pack()

option4 = Radiobutton(GUI, text="วาดไม้กายสิทธิ์และพยายามค้นหาที่มาของเสียง ", variable=var, value=4)
option4.pack()


# เฉลย
def ss_result():
    result = Toplevel()
    result.geometry("200x200")

    answer = var.get()
    data = v_name.get()
    
    if  answer == 1 :
        hat = PhotoImage(file="GUI--TK/NEW/กริฟฟินดอร์.gif")
        text = (data,'อยู่บ้านกริฟฟินดอร์')
        writecsv(text)
    elif answer == 2:
        hat = PhotoImage(file="GUI--TK/NEW/เรเวนคลอว์.gif")
        text = (data,'อยู่บ้านเรเวนคลอว์')
        writecsv(text)
    elif answer == 3:
        hat = PhotoImage(file="GUI--TK/NEW/ฮัฟเฟอร์พัฟ.gif")
        text = (data,'อยู่บ้านฮัฟเฟอร์พัฟ')
        writecsv(text)
    elif answer == 4:
        hat = PhotoImage(file="GUI--TK/NEW/สลิทเทอร์ริน.gif")
        text = (data,'สลิทเทอร์ริน')
        writecsv(text)
    label = Label(result, image=hat)
    v_name.set('')
    label.pack()

    result.mainloop()


submit_button = Button(GUI, text="ยืนยัน", command=ss_result)
submit_button.pack()



GUI.mainloop()