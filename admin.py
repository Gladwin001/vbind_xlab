
from tkinter import Frame, StringVar
from tkinter import ttk
import datetime

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
        self.error_message = ttk.Label(self, text='kindly fill the field.', foreground='red')
        self.no_of_entries = len(self.label_values)
        self.string_vars = [StringVar() for _ in range(self.no_of_entries)]
        # print(self.string_vars)
        self.widgets()

    def widgets(self):
        # ======= grid 14 x 3 =======
        for i, value in enumerate(self.label_values):
            ttk.Label(self, text=value, justify='left', padding=(10, 5, 10, 5)).grid(row=i, column=0, sticky='new')
            entry = ttk.Entry(self, textvariable=self.string_vars[i])
            entry.grid(row=i, column=1, padx=10, sticky='ew')
            entry.bind('<Return>', self.entry_next)

        self.save_btn = ttk.Button(self, text='Save', width=10, command=self.on_save)
        self.save_btn.grid(row=14, columnspan=2, padx=10, pady=10, sticky='e')
        self.save_btn.bind('<Return>', self.on_save)  
    
    def entry_next(self, event):
        next_entry = event.widget.tk_focusNext()
        next_entry.focus()
        if isinstance(next_entry, ttk.Entry):
            # select text only if the next widget is an entry.
            next_entry.select_range(0, 'end')
        return("break")

    def on_save(self, e=None):
        with open('admin_values.txt', 'a') as f:
            current_time=str(datetime.datetime.now())
            f.write(current_time)
            f.write("\n")
            counter=0
            values = []
            lst=[]
            for i in range(self.no_of_entries):
                self.error_message.grid_forget()   
                values.append(self.string_vars[i].get())
                
                # if values[i]<1000: 
                #     counter=counter+1
                #     self.error_message.grid_forget()
                # else:
                #     self.error.message.grid()   
            try :                
                lst=[float(n) for n in values]  
                self.error_message.grid_forget()
            except:
                self.error_message.grid()
                counter=1
                f.write("Bad Input\n")
            if counter!=1:
                f.write('\n'.join(values))
                f.write("\n \n")               
                       
           
    
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
    frame.show_frame()
    app.mainloop()
