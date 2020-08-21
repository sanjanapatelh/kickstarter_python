import tkinter as tk
from tkinter import *
from tkinter import ttk
from front_manager import *
from front_create import *
from front_sponser import *
from front_manager import *
from front_display import *

def  main_screen():
    global screen
    screen=Tk()
    screen.geometry("2000x1080")
    screen.title("Kickstarter")
    canvas=Canvas(screen,width=2000,height=1080,bg="lightblue")
    canvas.pack(fill=BOTH,expand=1)
    Label(canvas,text="Welcome to Kickstarter!!!",bg="lightblue",font=("calibri",18,"bold")).pack()
    Button(canvas,text="Manager",command=fmanager).pack(pady=80,padx=80)
    Button(canvas,text="Contributor ",command=fsponser).pack(pady=30,padx=150)
    Button(canvas,text="Start Something----->>!!!",command=fdisplay).pack(pady=50)
    Button(canvas,text="Create",command= fcreate).pack(pady=30,padx=80)

    screen.mainloop()
main_screen()
