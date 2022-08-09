from tkinter import *
from login import LoginFrame
from sidebar import SidebarFrame
from content import ContentFrame


class App(Tk):
    def __init__(self):
        super().__init__()
        self.window_configure()
        self.widgets()
    
    def widgets(self):
        # self.frames = [AdminFrame, ]

        self.login = LoginFrame(self)
        self.sidebar = SidebarFrame(self)
        self.content = ContentFrame(self)

        self.login.show_frame()

    def window_configure(self):
        self.title("X-LAB") #title of window
        self.geometry("900x500")
        self.propagate(False)

    def change_content_frame(self, e):
        self.content.show_frame(e['text'])
    
    def change_main_window(self, go_to_login=False):
        if go_to_login:
            self.login = LoginFrame(self)
            self.sidebar.destroy_frame()
            self.content.destroy_frame()
            self.login.show_frame()

        else:
            self.login.destroy_frame()
            self.sidebar.show_frame()
            self.content.show_frame()

if __name__ == "__main__":
  app = App()
  app.mainloop()
