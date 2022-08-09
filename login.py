from tkinter import Entry, Label, Frame
from tkinter.ttk import Button

class LoginFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
    
    def widgets(self):
        Label(self, text='Username').pack()
        Entry(self).pack()
        Label(self, text='Password').pack()
        Entry(self, show='*').pack()
        Button(self, text='Login', command=self.login_to_app).pack()
    
    def login_to_app(self):
        self.parent.change_main_window()
    
    def show_frame(self):
        self.pack(expand=True, fill='both')

    def hide_frame(self):
        self.pack_forget()
    
    def destroy_frame(self):
        self.destroy()

    
# for testing
if __name__ == "__main__":
    from tkinter import Tk
    app = Tk()
    app.geometry("900x500")
    frame = LoginFrame(app)
    frame.pack(expand=True, fill='both')
    app.mainloop()