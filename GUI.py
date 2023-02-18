from tkinter import *
from tkinter import ttk #ธีม
from tkinter import messagebox

GUI = Tk () #จอหลัก
GUI.title ('จะไปอยู่บ้านไหน') #ชื่อโปรแกรม
GUI.geometry('1000x500') #ขนาด


hat=PhotoImage(file="file.png")
lh=Label(GUI,image=hat)
lh.pack()

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
def show_result():
    result = Toplevel()
    result.geometry("200x200")

    answer = var.get()

    if  answer == 1 :
        hat = PhotoImage(file="กริฟฟินดอร์.gif")
    elif answer == 2:
        hat = PhotoImage(file="เรเวนคลอว์.gif")
    elif answer == 3:
        hat = PhotoImage(file="ฮัฟเฟอร์พัฟ.gif")
    elif answer == 4:
        hat = PhotoImage(file="สลิทเทอร์ริน.gif")
    label = Label(result, image=hat)
    label.pack()

    result.mainloop()


submit_button = Button(GUI, text="คัดสรร", command=show_result)
submit_button.pack()



GUI.mainloop()
