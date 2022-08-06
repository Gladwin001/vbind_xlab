from tkinter import Frame
from tkinter import ttk

class UserFrame(Frame):
    def __init__(self, parent, **args):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, minsize=20)
        self.grid_columnconfigure((0, 1, 2,3,4,5,6), weight=1)
        self.label_values = ['STD-1','STD-2','STD-3','STD-4','STD-5','STD-6','STD-7','STD-8','STD-9','STD-10']
        self.widgets()

    def entry_data(self, e=None):
        #entries_1=''
        entries_1=[]
        for value in self.data:
            #entries_1=entries_1+ int(value.get()) +'\n'
            entries_1.append(int(value.get()))

        print(entries_1)


    def widgets(self):
        self.data=[]
        for i, value in enumerate(self.label_values):
            ttk.Label(self, text=value, justify='left', padding=(10, 5, 10, 5)).grid(row=i, column=2, sticky='new')
        for i in range(10):
            entries=ttk.Entry(self)
            entries.grid(row=i, column=3, padx=10, sticky='ew')
            self.data.append(entries)

        self.save_btn = ttk.Button(self, text='Save', width=10,command=self.entry_data)
        self.save_btn.grid(row=10,  column=2,columnspan=2, padx=10, pady=10, sticky='e')
        self.save_btn.bind('<Return>', self.entry_data)

    def show_frame(self):
        self.pack(expand=True, fill='both')

    def hide_frame(self):
        self.pack_forget()

    def destroy_frame(self):
        self.destroy()


# For testing - Only run user.py to test this frame.
if __name__ == "__main__":
    from tkinter import Tk
    app = Tk()
    app.geometry("900x500")
    app.config(bg="white")
    frame = UserFrame(app)
    frame.pack(expand=True, fill='both')
    app.mainloop()
