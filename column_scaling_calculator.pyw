from tkinter import *
import math

class Calculator:
    def __init__(self):
        self.master = Tk()
        self.master.title("Column Scale Calculator")
        self.flowrate_2 = 0
        self.flowrate_1 =  0
        self.diameter_2 = 0
        self.diameter_1 = 0
        self.injection_volume_1 = 0
        self.length_2 = 0
        self.length_1  = 0
        self.namelist = ['I.D.(mm)', 'Length (mm)', 'Inj. volume (uL)', 'Flow rate (mL/min)', 'Column vol (mL)']
        self.y_list = ['','Column 1', 'Column 2']
        self.entry_boxes = []
        for y in range(3):
            labels = Label(self.master, text=self.y_list[y])
            labels.grid(column=0, row=y)
            if y == 0:
                for i in range(5):
                    labels = Label(self.master, text=self.namelist[i])
                    labels.grid(column=i+1, row=y)
            else:
                for i in range(5):
                    entry_box = Entry(self.master)
                    entry_box.grid(column=i+1, row=y, pady = 2, padx=1)
                    if len(self.entry_boxes)==4 or len(self.entry_boxes)>6:
                        entry_box.configure({"background": "lightgrey"})
                    self.entry_boxes.append(entry_box)
        ok_button = Button(self.master, text = "OK", command=self.calculate, width=10)
        ok_button.grid(row = 4, column = 0, rowspan=2, pady = 4, padx=5)
        self.scalig_label = Label(self.master, text=f"Scaling Factor:")
        self.scalig_label.grid(row = 4, column = 1)
        self.warnlabel = Label(self.master, text=(""))
        self.warnlabel.grid(row = 4, column = 4, sticky = W)
        self.master.bind('<Return>', self.calculate)
        
        self.master.mainloop()
        
    def calculate(self, *args): 
        self.warnlabel.configure(text="")
        try:
            self.flowrate_1 = float(self.entry_boxes[3].get()) 
            self.diameter_2 = float(self.entry_boxes[5].get())
            self.diameter_1 = float(self.entry_boxes[0].get())
            self.injection_volume_1 = float(self.entry_boxes[2].get())
            self.length_2 = float(self.entry_boxes[6].get())
            self.length_1  = float(self.entry_boxes[1].get())
        except ValueError:
            self.warnlabel.configure(text="Please enter values!")
            return None
        
        if self.flowrate_1 * self.diameter_2 * self.diameter_1 * self.injection_volume_1 * self.length_1 * self.length_2 == 0:
            return None
        self.flowrate_2 =  self.flowrate_1 * ((self.diameter_2**2)/(self.diameter_1**2))
        self.injection_volume_2 = self.injection_volume_1 * ((self.diameter_2**2)/(self.diameter_1**2)) * (self.length_2/self.length_1)
        scaling = round((self.diameter_2**2)/(self.diameter_1**2),1)
        column_volume_1 = (self.diameter_1/2)**2 * math.pi * self.length_1 / 1000
        column_volume_2 = (self.diameter_2/2)**2 * math.pi * self.length_2 / 1000
        self.entry_boxes[4].delete(0, END)
        self.entry_boxes[4].insert(0, round((column_volume_1), 1))
        self.entry_boxes[9].delete(0, END)
        self.entry_boxes[9].insert(0, round((column_volume_2), 1))
        self.entry_boxes[7].delete(0, END)
        self.entry_boxes[7].insert(0, round(self.injection_volume_2, 1))
        self.entry_boxes[8].delete(0, END)
        self.entry_boxes[8].insert(0, round(self.flowrate_2, 1))
        self.scalig_label.configure(text=f"Scaling Factor: {scaling}")
        
if __name__ == "__main__":      
    calc = Calculator()