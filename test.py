from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Labelframe
from PIL import ImageTk,Image

root=Tk()
root.title("X-LAB")
root.geometry("900x500")

welcomeFrame=LabelFrame(root,text="WELCOME",font=("market",20),background="#ffffff",width=600,height=700)

img= Image.open("welcome_img.jpg")
render = ImageTk.PhotoImage(img)
image = Label(welcomeFrame, image=render)
image.place(x=50, y=5)

welcomeFrame.pack(side=RIGHT,expand=TRUE,fill=BOTH)

standard=Labelframe(root,width=150,height=700)
standard.pack(side=LEFT)

button_admin = Button(standard, text=" ADMIN ",font=("Helvetica 15 bold"))
button_user = Button(standard, text="  USER  ",font=("Helvetica 15 bold"))

button_admin.place(x = 30, y = 100,height=30)
button_user.place(x = 30, y = 150,height=30)




root.mainloop()
