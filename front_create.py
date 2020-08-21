import tkinter as tk
from tkinter import ttk
from  abi import *
from deploy_newContract import *

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createForm()
    def createForm(self):
        self.createButton('Create New Contract',4,0,self.create)


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

    def create(self):
        self.my_address=tk.StringVar()
        self.createTextBox("Enter Your Address",8,0,self.my_address)
        self.value=tk.IntVar()
        self.createTextBox("Enter Minimum amount To contribute",12,0,self.value)
        self.description_startup=tk.StringVar()
        self.createTextBox("Enter Description",16,0,self.description_startup)
        self.createButton('Create',20,0,self.create_function)

    def create_function(self):
        def normalize_32_byte_hex_address(value):
            as_bytes = web3.eth.utils.to_bytes(hexstr=value)
            return web3.eth.utils.to_normalized_address(as_bytes[-20:])
        value_to_send=int("{}".format(self.value.get()))
        my_address_to_send=normalize_32_byte_hex_address(self.my_address.get())
        description_to_send="{}".format(self.description_startup.get())
        result=createNewContract(value_to_send,description_to_send,my_address_to_send)
        self.createTextBoxDisplay('Your Contract Address',result,24,0)
        lis=[self.description_startup,self.my_address,self.value]
        self.clear(lis)
        #lis=[self.contract_address,self.value,self.my_address]
        #self.clear(lis)




def fcreate():
    app=tk.Tk()
    app.geometry("2000x1082")
    root=Application(app)
    root.mainloop()
