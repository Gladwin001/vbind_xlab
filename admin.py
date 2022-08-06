from tkinter import Frame, StringVar
from tkinter import ttk


class AdminFrame(Frame):
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, padding=(20, 10))  # padding for Frame
        self.parent = parent
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, minsize=20)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_columnconfigure(2, weight=6)
        self.label_values = [
            'UNCER OF DMM UUC',
            'K FACTOR',
            'UNCER OF DMM STD',
            'UNCER OF SENSOR',
            'K FACTOR',
            'DRIFT OF SENSOR',
            'STABILITY OF FURN',
            'AXIAL UNIFORMITY',
            'RADIAL UNIFORMITY',
            'RESOLUTION',
            'AMBIENT CORRECTION',
            'TEMP. COEFF',
            'CAL.POINT',
        ]
        self.no_of_entries = len(self.label_values)
        self.string_vars = [StringVar() for _ in range(self.no_of_entries)]
        self.widgets()

    def widgets(self):
        # ======= grid 14 x 3 =======
        for i, value in enumerate(self.label_values):
            ttk.Label(self, text=value, justify='left', padding=(10, 5, 10, 5)).grid(row=i, column=0, sticky='new')
            ttk.Entry(self, textvariable=self.string_vars[i]).grid(row=i, column=1, padx=10, sticky='ew')

        self.save_btn = ttk.Button(self, text='Save', width=10, command=self.on_save)
        self.save_btn.grid(row=14, columnspan=2, padx=10, pady=10, sticky='e')
        self.save_btn.bind('<Return>', self.on_save)  
    
    def on_save(self, e=None):
        for i in range(self.no_of_entries):
            print(self.string_vars[i].get())
    
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
    frame = AdminFrame(app)
    frame.pack(expand=True, fill='both')
    app.mainloop()
