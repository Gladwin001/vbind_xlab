import imp
from tkinter import *
from tkinter import ttk
from sidebar import SidebarFrame
from admin import AdminFrame

if __name__ == '__main__':
    root=Tk()
    root.title("X-LAB")
    root.geometry("900x500")

    sidebar = SidebarFrame(root)
    
    root.mainloop()