import tkinter as tk
from tkinter import ttk
from  abi import *
from manager import *


class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createForm()
    def createForm(self):
        self.createButton('Manager',0,0,self.manager)

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

    def manager(self):
        self.contract_address=tk.StringVar()
        self.createTextBox("Enter Contract Address",4,0,self.contract_address)
        self.my_address=tk.StringVar()
        self.createTextBox("Enter Your Address",8,0,self.my_address)
        self.createButton('Get Your contract',14,0,self.validate_function)

    def validate_function(self):
        contract_address_to_Send="{}".format(self.contract_address.get())
        my_address_to_send="{}".format(self.my_address.get())
        if (validation(contract_address_to_Send,my_address_to_send)):
            self.getfunctions()
        else:
            tk.Label(self,text="Invalid User").grid(row=18,column=0,sticky=tk.W)


    def getfunctions(self):
        self.createButton('Create Request',16,0,self.createrequest)
        self.createButton('Finalize request',16,10,self.finalizerequest)
        self.createButton('Get Summary',16,30,self.getsummary)
        self.createButton('Get Summary Of Request',16,40,self.getsummaryrequest)


    def createrequest(self):
        self.description_temp=tk.StringVar()
        self.createTextBox("Enter description",18,0,self.description_temp)
        self.value=tk.IntVar()
        self.createTextBox("Enter amount To contribute",22,0,self.value)
        self.recipient_address=tk.StringVar()
        self.createTextBox("Enter Recipient Address",26,0,self.recipient_address)
        self.createButton('Create Request',30,0,self.createrequest_function)

    def createrequest_function(self):
        description_to_send="{}".format(self.description_temp.get())
        value_to_send=int("{}".format(self.value.get()))
        recipient_address_to_send="{}".format(self.recipient_address.get())
        contract_address_to_Send="{}".format(self.contract_address.get())
        createRequest(description_to_send,value_to_send,recipient_address_to_send,contract_address_to_Send)
        lis=[self.description_temp,self.value,self.recipient_address,self.contract_address,self.my_address]
        self.clear(lis)

    def finalizerequest(self):
        self.index=tk.IntVar()
        self.createTextBox("Enter Index of Request",18,10,self.index)
        self.createButton('Finalize',22,10,self.finalize_function)

    def finalize_function(self):
        contract_address_to_Send="{}".format(self.contract_address.get())
        index_to_send=int("{}".format(self.index.get()))
        finalizeRequest(index_to_send,contract_address_to_Send)
        lis=[self.contract_address,self.index,self.my_address]
        self.clear(lis)

    def getsummary(self):
        contract_address_to_Send="{}".format(self.contract_address.get())
        details=getSummary(contract_address_to_Send)
        self.createTextBoxDisplay('Description',details[0],18,20)
        self.createTextBoxDisplay('Minimum contribution required',details[1],22,20)
        self.createTextBoxDisplay('Balance_amount',details[2],24,20)
        self.createTextBoxDisplay('Number of requests present',details[3],28,20)
        self.createTextBoxDisplay('ApproversCount',details[4],32,20)
        self.createTextBoxDisplay('manager Addres',details[5],36,20)

    def getsummaryrequest(self):
        self.summaryindex=tk.IntVar()
        self.createTextBox("Enter Index of Request",18,30,self.summaryindex)
        self.createButton('Get Details',22,30,self.function_getsummaryrequest)


    def function_getsummaryrequest(self):
        contract_address_to_Send="{}".format(self.contract_address.get())
        index_to_send=int("{}".format(self.summaryindex.get()))
        details=request_details(index_to_send,contract_address_to_Send)
        self.createTextBoxDisplay('Description',details[0],24,30)
        self.createTextBoxDisplay('MMoney Needed',details[1],28,30)
        self.createTextBoxDisplay('Complete Status',details[2],30,30)
        self.createTextBoxDisplay('Number of approvals',details[3],32,30)


def fmanager():
    app=tk.Tk()
    app.geometry("2000x1082")
    root=Application(app)
    root.mainloop()
