from tkinter import *
from PIL import ImageTk, Image
from admin import AdminFrame


class SidebarFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width=150, height=700, background='#D9D9D9')
        self.parent = parent
        self.propagate(0)
        self.pack(side=LEFT, fill=Y)
        self.widgets()
    
    def widgets(self):
        self.user_icon = ImageTk.PhotoImage(Image.open('assets/icons/user_icon.png').resize((24, 24),Image.Resampling.LANCZOS)) # importing user_icon.png

        self.btn_admin = Button(self, text="Admin", font=("Helvetica 15"), relief='flat', overrelief='flat', background='#D9D9D9', command=self.show_admin)
        self.btn_admin.config(image=self.user_icon, compound='left') # icon
        self.btn_admin.pack(anchor='w', fill=X)
        self.btn_admin.bind("<Enter>", self.btn_hover_onenter)
        self.btn_admin.bind("<Leave>", self.btn_hover_onleave)

        self.btn_user = Button(self, text="User", font=("Helvetica 15"), relief='flat', overrelief='flat', background='#D9D9D9')
        self.btn_user.config(image=self.user_icon, compound='left') #icon
        self.btn_user.pack(anchor='w', fill=X, side=TOP)
        self.btn_user.bind("<Enter>", self.btn_hover_onenter)
        self.btn_user.bind("<Leave>", self.btn_hover_onleave)

    def btn_hover_onenter(self, e):
        e.widget['background'] = '#999999'

    def btn_hover_onleave(self, e):
        e.widget['background'] = '#D9D9D9'

    def show_admin(self):
        pass # To write code for showing Admin frame


    

#For Testing
if __name__ == '__main__':
    root=Tk()
    root.title("X-LAB")
    root.geometry("900x500")
    SidebarFrame(root)
    root.mainloop()