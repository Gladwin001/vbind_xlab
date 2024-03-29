from tkinter import Frame, DoubleVar ,IntVar, StringVar
from tkinter import ttk

from lib.scrollframe import VerticalScrolledFrame


class UserFrame(VerticalScrolledFrame):        #Main User Frame
    def __init__(self, parent, **args):
        VerticalScrolledFrame.__init__(self, parent)
        self.parent = parent

        self.widgets()
    
    def widgets(self):
        self.uf1 = UserFrame_std(self.interior, self)
        self.uf1.show_frame()
        self.uf2 = UserFrame_uuc(self.interior, self)
        self.uf2.show_frame()

    def get_true_value(self):
        return self.uf1.true_value_std
        
    def show_frame(self):
        self.pack(expand=True, fill='both')

    def hide_frame(self):
        self.pack_forget()

    def destroy_frame(self):
        self.destroy()



class UserFrame_std(Frame):        #STD Frame
    def __init__(self, parent_cont, parent):
        Frame.__init__(self, parent_cont, background="white")
        self.parent_cont = parent_cont
        self.parent = parent
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16), weight=1, minsize=20)
        self.grid_columnconfigure((0, 1, 2,3,4,5,6), weight=1)

        #==== VARIABLES =====

        # Standard Deviation Variables
        self.std_labels = ['STD-1','STD-2','STD-3','STD-4','STD-5','STD-6','STD-7','STD-8','STD-9','STD-10','AVG. STD','Ambient','Ambient correction','Error of DMM','Error of sensor', 'True Value in STD']
        self.std_vars = [StringVar()for i in range(len(self.std_labels))]
        
        self.data=[]
        #====================
        self.widgets()
        
    def widgets(self):
        for i, value in enumerate(self.std_labels):
            ttk.Label(self, text=value, justify='left', padding=(10, 5, 10, 5)).grid(row=i, column=1, sticky='new')
        for i in range(len(self.std_labels)):
            if i in (10, 15):
                label = ttk.Label(self)
                label.grid(row=i, column=2, padx=10, sticky='ew')
                self.data.append(label)
                continue
            entry=ttk.Entry(self, textvariable=self.std_vars[i])
            entry.grid(row=i, column=2, padx=10, sticky='ew')
            entry.bind('<Return>', self.entry_next)
            entry.bind('<FocusOut>', self.calculate_avg)
            # entry.bind('<FocusIn>', self.select_widget)
            self.data.append(entry)

        self.save_btn = ttk.Button(self, text='Save', width=10, command=self.on_save)
        self.save_btn.grid(columnspan=3, padx=10, pady=10, sticky='e')
        self.save_btn.bind('<Return>', self.on_save)
        
    def on_save(self, e=None):
        true_value_std_c= float(self.data[10]['text']) + float(self.std_vars[12].get()) - float(self.std_vars[13].get())
        #print("\n The true value in celsius is ",true_value_std_c)                #true value of std in celsius
        self.true_value_std=true_value_std_c - float(self.std_vars[14].get())
        print("\n The true value of std is ",self.true_value_std)
        self.data[15]['text'] = round(self.true_value_std, 2)
        
    def calculate_avg(self, *args):
        summ = 0.0
        for  i in range(10):
            val = self.std_vars[i].get()
            if val == '':
                summ += 0
                continue
            summ += float(self.std_vars[i].get())
        self.data[10]['text'] = str(summ/10.0)

    def entry_next(self, event):
        next_entry = event.widget.tk_focusNext()
        next_entry.focus()
        if isinstance(next_entry, ttk.Entry):
            # select text only if the next widget is an entry.
            next_entry.select_range(0, 'end')
        return("break")
    
    # def select_widget(self ,e):
    #     e.widget.select_range(0, 'end')

    def show_frame(self):
        self.pack(expand=True, fill='both')

    def hide_frame(self):
        self.pack_forget()

    def destroy_frame(self):
        self.destroy()

class UserFrame_uuc(Frame):      #UUC Frame
    def __init__(self, parent_cont, parent):
        Frame.__init__(self, parent_cont, background="white")
        self.parent_cont = parent_cont
        self.parent = parent
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), weight=1, minsize=20)
        self.grid_columnconfigure((0, 1, 2,3,4,5,6), weight=1)

        #==== VARIABLES =====
        # Standard Deviation Variables
        self.uuc_labels = ['UUC-1','UUC-2','UUC-3','UUC-4','UUC-5','UUC-6','UUC-7','UUC-8','UUC-9','UUC-10','AVG. UUC','Ambient','Ambient correction','Error of DMM', 'True Value in UUC', 'Final Error']
        self.uuc_vars = [StringVar()for i in range(len(self.uuc_labels))]
        self.data=[]
        #====================
        self.widgets()
        
    def widgets(self):
        for i, value in enumerate(self.uuc_labels):
            ttk.Label(self, text=value, justify='left', padding=(10, 5, 10, 5)).grid(row=i, column=1, sticky='new')
        for i in range(len(self.uuc_labels)):
            if i in (10, 14, 15):
                label = ttk.Label(self)
                label.grid(row=i, column=2, padx=10, sticky='ew')
                self.data.append(label)
                continue
            entry=ttk.Entry(self, textvariable=self.uuc_vars[i])
            entry.grid(row=i, column=2, padx=10, sticky='ew')
            entry.bind('<Return>', self.entry_next)
            entry.bind('<FocusOut>', self.calculate_avg)
            # entry.bind('<FocusIn>', self.select_widget)
            self.data.append(entry)

        self.save_btn = ttk.Button(self, text='Save', width=10, command=self.on_save)
        self.save_btn.grid( columnspan=3, padx=10, pady=10, sticky='e')
        self.save_btn.bind('<Return>', self.on_save)
        #self.save_btn.bind('<Return>', self.difference,add='+')
   
    def on_save(self, e=None):
        true_value_uuc_c= float(self.data[10]['text']) + float(self.uuc_vars[12].get()) - float(self.uuc_vars[13].get())
        print("\n The true value of uuc in celsius is ",round(true_value_uuc_c, 2))   #true value of uuc in celsius
        print("\n The conversion to celsius is ",round(true_value_uuc_c, 2)) 
        # true_value_std = UserFrame_std.on_save()
        final_error = true_value_uuc_c - self.parent.get_true_value()           # [final error=conversion to celsius - true value of std]
        print("\n The final error ",round(final_error, 2))      #final error which is to be displayed in report
        self.data[14]['text'] = round(true_value_uuc_c, 2)
        self.data[15]['text'] = round(final_error, 2)
        report_file = open("report_variables.txt", "w")     # To write a values needed in report in report_variables.txt file
        report_file.seek(0)           # To bring cursor to first line              
        report_file.truncate()        # To clear all contents of the file
        report_file.write(str(round(self.parent.get_true_value(),2))+"\n")
        report_file.write(str(round(true_value_uuc_c,2))+"\n")
        report_file.write(str(round(final_error,2))+"\n")
        report_file.write('0.67')




            
    def entry_next(self, event):
        next_entry = event.widget.tk_focusNext()
        next_entry.focus()
        if isinstance(next_entry, ttk.Entry):
            # select text only if the next widget is an entry.
            next_entry.select_range(0, 'end')
        return("break")

    def difference(self,e=None) :
        arr=[DoubleVar()for i in range(10)]
        for i in range(0,10,1):
            arr[i]=UserFrame_std.uuc_vars[i].get() - UserFrame_std.std_vars[i].get()
        print(arr)
    
    def calculate_avg(self, *args):
        summ = 0.0
        for  i in range(10):
            val = self.uuc_vars[i].get()
            if val == '':
                summ += 0
                continue
            summ += float(self.uuc_vars[i].get())
        self.data[10]['text'] = str(summ/10.0)
    
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
    app.geometry("600x2000")
    app.config(bg="white")
    #scrollbar = ttk.Scrollbar(app, orient='vertical', command=app.yview)
    #scrollbar.grid(row=0, column=1, sticky='NS')
    #app['yscrollcommand'] = scrollbar.set
    frame = UserFrame(app)
    frame.show_frame()
    app.mainloop()