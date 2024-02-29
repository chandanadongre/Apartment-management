from tkinter import *
from tkinter import messagebox

w=Tk()
w.geometry('900x700')
w.title("MENU")
#w.resizable(False,False)

j=0
r=0
for i in range(50):
   c=str(222222+r)
   Frame(w,width=900,height=700,bg='#'+c).place(x=j,y=0)
   j=j+10
   r=r+1

Frame(w,width=500,height=600,bg='lavender').place(x=430,y=50)
def display():
   import projectdata
def add():
   import projectadd
def notpaid():
   import notpaidgui2
  
def paid():
   import paidgui
   
def removeresident():
   import remove
   


#Welcome label
k=Label(w,text="Welcome  to Sumukha tropicals",bg="lavender")
k1=("Lucida Calligraphy",20)
k.config(font=k1,foreground="Navy blue")
k.place(x=450,y=120)


#Button 1
b1=Button(w,text="Display resident details ",command=display)
b=("Lucida Calligraphy",13)
b1.config(font=b,foreground="Maroon")
b1.place(x=490,y=200)

#Button 2
b2=Button(w,text="Add new resident details ",command=add)
b=("Lucida Calligraphy",13)
b2.config(font=b,foreground="Maroon")
b2.place(x=490,y=250)

b3=Button(w,text="Display residents who haven't paid ",command=notpaid)
b=("Lucida Calligraphy",13)
b3.config(font=b,foreground="Maroon")
b3.place(x=490,y=300)

b4=Button(w,text="Display residents who have paid  ",command=paid)
b=("Lucida Calligraphy",13)
b4.config(font=b,foreground="Maroon")
b4.place(x=490,y=350)

b5=Button(w,text="Remove resident details ",command=removeresident)
b=("Lucida Calligraphy",13)
b5.config(font=b,foreground="Maroon")
b5.place(x=490,y=400)
'''
b6=Button(w,text="Pay maintanence ",command=pay)
b=("Lucida Calligraphy",13)
b6.config(font=b,foreground="Maroon")
b6.place(x=490,y=450)
'''
w.mainloop()



