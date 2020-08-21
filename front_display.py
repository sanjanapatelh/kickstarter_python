import tkinter as tk
from tkinter import ttk
from  abi import *
from display import *
from manager import *

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createForm()

    def createButton(self,text_name,row,col,function):
        tk.Button(self,text=text_name,command=function).grid(row=row,column=col,sticky=tk.W)

    def createTextBox(self,text_name,row,col,variable):
        tk.Label(self,text=text_name).grid(row=row,column=col,sticky=tk.W)
        tk.Entry(self,textvariable=variable,width=30).grid(row=row,column=col+1,sticky=tk.W)

    def createTextBoxDisplay(self,text_name,text_value,row,col):
        tk.Label(self,text=text_name).grid(row=row,column=col,sticky=tk.W)
        tk.Label(self,text=text_value).grid(row=row,column=col+2,sticky=tk.W)


    def clear(self,lis):
        for i in lis:
            i.set("")


    def createForm(self):
        details_list = display()
        temp_row=5
        temp_col=5
        for startups in details_list:
            details=getSummary(startups)
            self.createTextBoxDisplay('Description',details[0],temp_row+2,temp_col)
            self.createTextBoxDisplay('Minimum contribution required',details[1],temp_row+4,temp_col)
            self.createTextBoxDisplay('Balance_amount',details[2],temp_row+6,temp_col)
            self.createTextBoxDisplay('Number of requests present',details[3],temp_row+8,temp_col)
            self.createTextBoxDisplay('ApproversCount',details[4],temp_row+10,temp_col)
            self.createTextBoxDisplay('manager Addres',details[5],temp_row+12,temp_col)
            self.createTextBoxDisplay('------------------------',"------------------------",temp_row+14,temp_col)
            temp_row=temp_row+16

def fdisplay():
    app=tk.Tk()
    app.geometry("2000x1082")
    root=Application(app)
    root.mainloop()
