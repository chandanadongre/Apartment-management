'''
from tkinter import *
class Grid:
    def __init__(self,w):
        for i in range(total_rows):
            for j in range(total_columns):
                self.l1=Label(w,text=notpaid_l[i][j], width=20, fg='maroon', bg='wheat1',font=(15))
                self.l1.grid(row=i, column=j)
def back():
    w.destroy()
    import projectlogin
    
with open('PYTHON.txt','r') as f:
    L=f.readlines()
    M=[]
    
    print(L)
    for i in L:
        M.append(i.split())
    paid_l,notpaid_l=[M[0]],[M[0]]
    print(M)
    print(L[0])
    for i in range(1,len(M)):
        if M[i][6]=='notpaid':
            print(L[i])
            notpaid_l.append(M[i])
        else:
            print(L[i])
            paid_l.append(M[i])
print(notpaid_l)

print("L is\n\n", L)
m=[i.split("\n") for i in L]#List of resident details
print("\n m is \n\n",m)
n=[j for i in range(len(m)) for j in m[i] if "notpaid" in j]# List of unpaid users
print("\n n is\n\n", n)


#2
print("Not paid")
for i in n:
    print(i)
print()
total_rows = len(n)
total_columns = len(n[0])

w=Tk()
w.title("Resident Details")
w.configure(background='sky blue')

Button(w, text='BACK',command=back).place(x=0,y=0)

t=Grid(w)
l1=Label(w,text="Residents With Due Payment",font=("bold",35))
l1.pack()
l1.config(bg= "SlateBlue4", fg= "white")
Button(w, text='BACK',command=back).place(x=0,y=0)
w.mainloop()
'''
with open('PYTHON.txt','r') as f:
    L=f.readlines()
    
m=[i.split("\n") for i in L]#List of resident details
n=[j for i in range(len(m)) for j in m[i] if "notpaid" in j]# List of unpaid users

from tkinter import *
from tkinter import messagebox

w=Tk()
w.geometry('900x700')
w.title("Notpaid")

j=0
r=0
for i in range(50):
   c=str(222222+r)
   Frame(w,width=900,height=700,bg='#'+c).place(x=j,y=0)
   j=j+10
   r=r+1

Frame(w,width=600,height=600,bg='lavender').place(x=400,y=50)
k=Label(w,text="Residents who haven't paid",bg="lavender")
k1=("Lucida Calligraphy",20)
k.config(font=k1)
k.place(x=420,y=70)
j=120
for i in range(len(n)):
    s=Label(w,text=n[i],bg="lavender")
   
    s1=("Lucida Calligraphy",10)
    s.config(font=s1)
    s.place(x=430,y=j)
    j+=40
    print(s)

w.mainloop()
