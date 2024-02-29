from tkinter import *
from tkinter import messagebox as mb
import os

def x():
    import projectlogin
def y():
    w.destroy()
def removal():
    print(t1.get())
    if t1.get()=='':
        mb.showinfo("Empty Input", "Input cannot be empty\nTry Again")
    else:
        flag=False
        
        for i in range(len(M)):
            if M[i][1]!=t1.get().rstrip():
                f2.write(L[i])
            else:
                flag=True

        
        f1.close()
        f2.close()
        os.replace('newdata.txt','data.txt')

        if flag==False:
            mb.showinfo("Invalid Input", "Flat Number Not Found\nTry Again")
            w.destroy()
            import projectlogin
        else:
            mb.showinfo("Success", "Resident Details successfully removed")
            w.destroy()
            import projectlogin
w=Tk()
#Label(w,text='Prestige Apartment').place(x=0,y=350)

w.geometry("1000x800")
bg=PhotoImage(file='prestige.gif')
label=Label(w,image=bg)
label.place(x=0,y=0)

l1=Label(w,text="Delete Resident Details",font=("bold",35))
l=("Academy Engraved LET",36)
l1.config(font=l,bg= "midnight blue", fg= "white")
l1.place(x=180,y=100)

l2=Label(w,text='Enter flat number to be deleted',font=("bold",25))
l2.config(font=l,bg= "deep sky blue", fg= "white")
l2.place(x=180,y=200)

p1 = PhotoImage(file="sumukha.gif")

t1=Entry(w)
t1.place(x=180,y=350)

f1=open("data.txt",'r')
f2=open("newdata.txt",'w')
L=f1.readlines()
M=[]
for i in L:
    M.append(i.split())
    
b2=Button(w,text="Click Here to Delete ",wraplength=200,command=removal)
b=("Academy Engraved LET",36)
b2.config(font=b)
b2.place(x=180,y=500)

'''
b1=Button(w,width=150,height=150,bg='red',command=x)
b1.place(x=150,y=400)
'''
w.mainloop()
