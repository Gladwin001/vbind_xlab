from tkinter import Frame, IntVar
from tkinter import ttk

class UserFrame(Frame):
    def __init__(self, parent, **args):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, minsize=20)
        self.grid_columnconfigure((0, 1, 2,3,4,5,6), weight=1)

        #==== VARIABLES =====

        # Standard Deviation Variables
        self.std_labels = ['STD-1','STD-2','STD-3','STD-4','STD-5','STD-6','STD-7','STD-8','STD-9','STD-10']
        self.std_vars = [IntVar()for i in range(len(self.std_labels))]
        
        #====================
        self.widgets()
        
    def widgets(self):
        self.data=[]
        self.entries=[]
        for i, value in enumerate(self.std_labels):
            ttk.Label(self, text=value, justify='left', padding=(10, 5, 10, 5)).grid(row=i, column=2, sticky='new')
        for i in range(len(self.std_labels)):
            entry=ttk.Entry(self, textvariable=self.std_vars[i])
            entry.grid(row=i, column=3, padx=10, sticky='ew')
            self.data.append(entry)

        self.save_btn = ttk.Button(self, text='Save', width=10, command=self.on_save)
        self.save_btn.grid(row=10, columnspan=4, padx=10, pady=10, sticky='e')
        self.save_btn.bind('<Return>', self.on_save)
        
    def on_save(self, e=None):
        # write code after clicking the button
        # below code is printing all the values entered in the entries at the time of clicking 'save' btn.
        sum=0
        for i in range(len(self.std_labels)):
            print(float(self.std_vars[i].get()),end='\t')
            sum=sum+self.std_vars[i].get()
        avg=sum/len(self.std_labels)
        return(avg)
        #print('The average is',avg)
    def show_frame(self):
        self.pack(expand=True, fill='both')

    def hide_frame(self):
        self.pack_forget()

    def destroy_frame(self):
        self.destroy()

class UserFrame_1(Frame):
    def __init__(self, parent, **args):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.grid_rowconfigure(( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, minsize=20)
        self.grid_columnconfigure((0, 1, 2,3,4,5,6), weight=1)

        self.std_labels=['Ambient','Ambient correction','Error of DMM']
        self.std_vars = [IntVar()for i in range(len(self.std_labels))]
        self.widgets()
    def widgets(self):
        self.data=[]
        self.entries=[]
        for i, value in enumerate(self.std_labels):
            ttk.Label(self, text=value, justify='left', padding=(10, 5, 10, 5)).grid(row=i, column=2, sticky='new')
        for i in range(len(self.std_labels)):
            entry=ttk.Entry(self, textvariable=self.std_vars[i])
            entry.grid(row=i, column=3, padx=10, sticky='ew')
            self.data.append(entry)

        self.save_btn = ttk.Button(self, text='Calculate', width=10,command=self.on_save)
        self.save_btn.grid(row=3, columnspan=4, padx=10, pady=10,sticky='e')
        self.save_btn.bind('<Return>', self.on_save)
    
    def on_save(self, e=None):
        #avg=IntVar()
        print('\n')
        for i in range(len(self.std_labels)):
            print(float(self.std_vars[i].get()), end='\t')
        # error!!!!! try to bring value of standard average
        avg=frame.on_save()
        true_value_c= avg + self.std_vars[1] - self.std_vars[2]
        print(true_value_c)



# For testing - Only run user.py to test this frame.
if __name__ == "__main__":
    from tkinter import Tk
    app = Tk()
    app.geometry("600x1000")
    app.config(bg="white")
    frame = UserFrame(app)
    frame.pack(expand=True, fill='both')
    frame_1=UserFrame_1(app)
    frame_1.pack(expand=True, fill='both')
    app.mainloop()