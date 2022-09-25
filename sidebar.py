from tkinter import Frame, Button
from tkinter.ttk import Label
from PIL import ImageTk, Image
from admin import AdminFrame
# from content import ContentFrame


class SidebarFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width=150,
                       height=700, background='#D9D9D9')
        self.parent = parent

        # =====VARIABLES=====
        self.sidebar_current_width = 150
        self.is_sidebar_extended = True
        # ===================

        self.propagate(0)
        self.widgets()

    def widgets(self):
        self.user_icon = ImageTk.PhotoImage(Image.open('assets/icons/user_icon.png').resize((24, 24), Image.LANCZOS))  # importing user_icon.png
        
        self.create_sidebar_handler() # hamburger icon
        self.btn_admin = self.add_btn(text="Admin", img=self.user_icon)
        self.btn_user = self.add_btn(text="User", img=self.user_icon)

    def toggle_sidebar(self, e=None):
        if self.is_sidebar_extended:
            self.sidebar_current_width -= 20
            self.config(width=self.sidebar_current_width)
            self.btn_ham.pack(anchor='center')
            self.btn_admin.pack_forget()
            self.btn_user.pack_forget()
            if self.sidebar_current_width == 50:
                self.btn_ham.config(image=self.hamburger_icon)
                self.is_sidebar_extended = False
                return
            self.after(5, self.toggle_sidebar)
        else:
            self.sidebar_current_width += 20
            self.config(width=self.sidebar_current_width)
            self.btn_ham.pack(anchor='e', fill='none')
            self.btn_admin.pack(anchor='w', fill='x')
            self.btn_user.pack(anchor='w', fill='x')
            if self.sidebar_current_width == 150:
                self.btn_ham.config(image=self.close_icon)
                self.is_sidebar_extended = True
                return
            self.after(5, self.toggle_sidebar)

    def btn_hover_onenter(self, e):
        e.widget['background'] = '#999999'

    def btn_hover_onleave(self, e):
        e.widget['background'] = '#D9D9D9'

    def add_btn(self, text=None, img=None, hover=True, **args):
        btn = Button(self, font=("Helvetica 15"), relief='flat', overrelief='flat',
                     background='#D9D9D9', borderwidth=0, command=lambda: self.send_signal_to_main(btn))
        if text and img:
            btn.config(text=text, image=img, compound='left')
        elif text:
            btn.config(text=text)  # ham
        elif img:
            btn.config(image=img)  # icon
        btn.pack(anchor='w', fill='x')
        if hover:
            btn.bind("<Enter>", self.btn_hover_onenter)
            btn.bind("<Leave>", self.btn_hover_onleave)
        return btn

    def send_signal_to_main(self, btn):
        self.parent.change_content_frame(btn)
    
    def create_sidebar_handler(self):
        self.hamburger_icon = ImageTk.PhotoImage(Image.open('assets/icons/hamburger.png').resize((30, 30), Image.LANCZOS))  # importing hamburger.png
        
        self.close_icon = ImageTk.PhotoImage(Image.open('assets/icons/close.png').resize((30, 30), Image.LANCZOS))  # importing hamburger.png

        self.btn_ham = Label(self, image=self.hamburger_icon, relief='flat', borderwidth=0, background='#D9D9D9')
        self.btn_ham.bind('<Button-1>', self.toggle_sidebar)
        self.btn_ham.bind("<Enter>", self.btn_hover_onenter)
        self.btn_ham.bind("<Leave>", self.btn_hover_onleave)
        self.btn_ham.pack(anchor='e', padx=5, pady=2)
    
    def show_frame(self):
        self.pack(side='left', fill='y')
    
    def hide_frame(self):
        self.pack_forget()
    
    def destroy_frame(self):
        self.destroy()


# For Testing
if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    root.title("X-LAB")
    root.geometry("900x500")
    sbf = SidebarFrame(root)
    sbf.show_frame()
    root.mainloop()
