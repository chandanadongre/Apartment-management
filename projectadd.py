from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to SUMUKHA TROPICALS")
window.geometry('400x400')
window.configure(background = "lavender");
a = Label(window ,text = "SRN No").grid(row = 0,column = 0)
b = Label(window ,text = "Flat No").grid(row = 1,column = 0)
c = Label(window ,text = "First Name").grid(row = 2,column = 0)
d = Label(window ,text = "Last Name").grid(row = 3,column = 0)
e = Label(window ,text = "Mobile Number").grid(row=4,column = 0)
f = Label(window ,text = "User Id").grid(row=5,column=0)
g = Label(window ,text = "Status").grid(row=6,column=0)
A = Entry(window)
A.grid(row = 0,column = 1)
B = Entry(window)
B.grid(row = 1,column = 1)
C = Entry(window)
C.grid(row = 2,column = 1)
D = Entry(window)
D.grid(row = 3,column = 1)
E = Entry(window)
E.grid(row = 4,column = 1)
F = Entry(window)
F.grid(row = 5,column = 1)
G = Entry(window)
G.grid(row = 6,column = 1)
s=A.get()
r=B.get()
t=C.get()
m=D.get()
n=E.get()
o=F.get()
p=G.get()
'''z=open("PYTHON.txt","a")
z.write(s,"\t",r,"\t",t,"\t",m,"\t",n,"\t",o,"\t",p,"\n")'''



'''s=65
L=[]
for i in range(6):
    v=chr(s).get()
    L.append(v)
    s=s+1
print(L)'''

def clicked():
   res = "Welcome to " + A.get()
   #lbl.configure(text= res)
   l1 = Label(window ,text = A.get()).grid(row=16,column=0)
btn = ttk.Button(window ,text="Submit", command= clicked).grid(row=8,column=0)
window.mainloop()

'''#to append the data user gave
f.open("PYTHON.txt","w")
f.close()
y=[]
for i in range(len(paid)):
    y.append(paid[i].split())
print(y)
print("Residents who have paid :")
for i in y:
    print(i[1])'''
