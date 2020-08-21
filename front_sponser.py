import tkinter as tk
from tkinter import ttk
from  abi import *
from sponsers import *

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createForm()
    def createForm(self):
        self.createButton('Sponser',0,0,self.sponser)

    def createButton(self,text_name,row,col,function):
        tk.Button(self,text=text_name,command=function).grid(row=row,column=col,sticky=tk.W)

    def createTextBox(self,text_name,row,col,variable):
        tk.Label(self,text=text_name).grid(row=row,column=col,sticky=tk.W)
        tk.Entry(self,textvariable=variable,width=30).grid(row=row,column=col+1,sticky=tk.W)

    def sponser(self):
        self.createButton('Contribute',2,0,self.contributor)
        self.createButton('Approve Request',2,5,self.approve)

    def contributor(self):
        self.contract_address=tk.StringVar()
        self.createTextBox("Enter Contract Address",4,0,self.contract_address)
        self.value=tk.IntVar()
        self.createTextBox("Enter amount To contribute",8,0,self.value)
        self.my_address=tk.StringVar()
        self.createTextBox("Enter Your Address",12,0,self.my_address)
        self.createButton('Contribute',14,0,self.contribute_function)

    def approve(self):
        self.approve_contract_address=tk.StringVar()
        self.createTextBox("Enter Contract Address",4,10,self.approve_contract_address)
        self.approve_my_address=tk.StringVar()
        self.createTextBox("Enter Your Address",12,10,self.approve_my_address)
        self.index=tk.IntVar()
        self.createTextBox("Enter Index of Request",8,10,self.index)
        self.createButton('Approve',14,10,self.approve_function)

    def contribute_function(self):
        contract_address_to_Send="{}".format(self.contract_address.get())
        value_to_send=int("{}".format(self.value.get()))
        my_address_to_send="{}".format(self.my_address.get())
        to_contribute(contract_address_to_Send,my_address_to_send,value_to_send)
        lis=[self.contract_address,self.value,self.my_address]
        self.clear(lis)


    def approve_function(self):
        contract_address_to_Send="{}".format(self.approve_contract_address.get())
        index_to_send=int("{}".format(self.index.get()))
        my_address_to_send="{}".format(self.approve_my_address.get())
        to_approve(contract_address_to_Send,my_address_to_send,index_to_send)
        lis=[self.approve_contract_address,self.index,self.approve_my_address]
        self.clear(lis)

    def clear(self,lis):
        for i in lis:
            i.set("")




def fsponser():
    app=tk.Tk()
    app.geometry("2000x1082")
    root=Application(app)
    root.mainloop()
