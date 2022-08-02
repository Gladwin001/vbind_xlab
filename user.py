from tkinter import Frame
from tkinter import ttk

class UserFrame(Frame):
    def __init__(self, parent, **args):
        Frame.__init__(self, parent, background="#9272BD")
        self.parent = parent
        self.widgets()
  
    def widgets(self):
        # Write UI code here with master attribute as self.
        # Use ttk.button for default system style.
        pass

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
    frame = UserFrame(app)
    frame.pack(expand=True, fill='both')
    app.mainloop()