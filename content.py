from inspect import currentframe
from tkinter import Frame
from admin import AdminFrame
from user import UserFrame

class ContentFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='#444', width=750)
        self.parent = parent
        self.widgets()
        self.pack_propagate(False)
    
    def widgets(self):
        self.current_child_frame = None
        # self.frames = {'Admin': AdminFrame(self),
        #                 'User': UserFrame(self),
        #                 }
        self.admin = AdminFrame(self)
        self.user = UserFrame(self)
    
    def show_frame(self, frame=None):
        if frame and self.current_child_frame is None:
            if frame=='Admin':
                self.admin.show_frame()
                self.current_child_frame = self.admin
            elif frame=='User':
                self.user.show_frame()
                self.current_child_frame = self.user

        elif frame=='Admin' and self.current_child_frame:
            self.current_child_frame.hide_frame()
            self.admin.show_frame()
            self.current_child_frame = self.admin

        elif frame=='User' and self.current_child_frame:
            self.current_child_frame.hide_frame()
            self.user.show_frame()
            self.current_child_frame = self.user
    
    def show_frame(self):
        self.pack(side='right', expand=True, fill='both')

    def hide_frame(self):
        self.pack_forget()
    
    def destroy_frame(self):
        self.destroy()

        




#For Testing
if __name__ == '__main__':
    from tkinter import Tk
    root=Tk()
    root.title("X-LAB")
    root.geometry("900x500")
    ContentFrame(root)
    root.mainloop()