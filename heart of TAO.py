import turtle
tao = turtle.Pen()
tao.shape('turtle')

#กำหนดสี
tao.speed (10)
tao.color("black", "red")
tao.begin_fill()
#กำหนดการเดิน
tao.penup()
tao.goto(0,100)
tao.pendown()
#ครึ่งหัวใจแรก
tao.left (120)
tao.circle(120, 190)
tao.forward(304.685)

#ครึ่งหัวใจท้าย
tao.left(100)
tao.forward(304.685)
tao.circle(120, 190)
tao.penup()
tao.home ()  #กลับเข้าบ้าน

tao.end_fill()

tao.done()
