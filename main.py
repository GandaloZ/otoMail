from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry("500x500")

musteriler = ['Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift']

var = Variable(value=musteriler)

listboxCustomers = Listbox(master, selectmode="multiple" ,listvariable=var, height=15, width=20)
listboxCustomers.place(x=5,y=5)

selectedListboxCustomers = Listbox(master, height=15, width=20)
selectedListboxCustomers.place(x=255,y=5)

def selectCustomer():
    for item in listboxCustomers.curselection():
        selectedListboxCustomers.insert("end", listboxCustomers.get(item))
        listboxCustomers.delete(item)

Button(master,text="--->",command=selectCustomer).place(x=150,y=35)
Button(master,text="<---").place(x=150,y=100)

mainloop()
