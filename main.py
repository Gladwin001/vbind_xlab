from tkinter import *
from sidebar import SidebarFrame
from content import ContentFrame


class App(Tk):
    def __init__(self):
        super().__init__()
        self.window_configure()
        self.widgets()
    
    def widgets(self):
        # self.frames = [AdminFrame, ]

        self.sidebar = SidebarFrame(self)
        self.content = ContentFrame(self)

    def window_configure(self):
        self.title("X-LAB") #title of window
        self.geometry("900x500")
        self.propagate(False)

    def change_content_frame(self, e):
        self.content.show_frame(e['text'])

if __name__ == "__main__":
  app = App()
  app.mainloop()
