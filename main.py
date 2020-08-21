from  abi import *
from display import *
from sponsers import *
from manager import *
#display()

while True:
    a=int(input("1.display\n2.contributor\n3.manager\n"))
    if a==1:
        display()
    elif a==2:
        call_startup_to_intaract()
    elif a==3:
        manager()
