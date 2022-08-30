from tkinter import Entry, Label, Frame
from tkinter.ttk import Button

USERNAME = '' # admin
PASSWORD = '' # admin@123

class LoginFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.widgets()
    
    def widgets(self):
        Label(self, text='Username').pack()
        self.username = Entry(self)
        self.username.pack()
        Label(self, text='Password').pack()
        self.password = Entry(self, show='*')
        self.password.pack()
        self.error_message = Label(self, text='Wrong username and password.', foreground='red')
        Button(self, text='Login', command=self.validate_login).pack()
    
    def login_to_app(self):
        self.parent.change_main_window()
    
    def validate_login(self):
        if self.username.get() == USERNAME and self.password.get() == PASSWORD:
            self.error_message.pack_forget()
            self.login_to_app()
        else:
            self.error_message.pack()
    
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