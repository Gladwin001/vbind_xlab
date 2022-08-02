from tkinter import Frame, Button
from PIL import ImageTk, Image
from click import command
from admin import AdminFrame
from content import ContentFrame


class SidebarFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width=150, height=700, background='#D9D9D9')
        self.parent = parent
        self.propagate(0)
        self.pack(side='left', fill='y')
        self.widgets()
    
    def widgets(self):
        self.user_icon = ImageTk.PhotoImage(Image.open('assets/icons/user_icon.png').resize((24, 24),Image.Resampling.LANCZOS)) # importing user_icon.png

        self.btn_admin = self.add_btn(text="Admin", img = self.user_icon)
        self.btn_user = self.add_btn(text="User", img = self.user_icon)

    def btn_hover_onenter(self, e):
        e.widget['background'] = '#999999'

    def btn_hover_onleave(self, e):
        e.widget['background'] = '#D9D9D9'

    def add_btn(self, text="Item", img=None, **args):
        btn = Button(self, text=text, font=("Helvetica 15"), relief='flat', overrelief='flat', background='#D9D9D9', command=lambda:self.send_signal_to_main(btn))
        if img:
            btn.config(image=img, compound='left') #icon
        btn.pack(anchor='w', fill='x')
        btn.bind("<Enter>", self.btn_hover_onenter)
        btn.bind("<Leave>", self.btn_hover_onleave)
        return btn

    def send_signal_to_main(self, e):
        self.parent.change_content_frame(e)



    

#For Testing
if __name__ == '__main__':
    from tkinter import Tk
    root=Tk()
    root.title("X-LAB")
    root.geometry("900x500")
    SidebarFrame(root)
    root.mainloop()