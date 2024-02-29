o='''
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
    notpaid_l,Paid_l=[M[0]],[M[0]]
    print(M)
    print(L[0])
    for i in range(1,len(M)):
        if M[i][6]=='notpaid':
            print(L[i])
            Paid_l.append(M[i])
        else:
            print(L[i])
            notpaid_l.append(M[i])
print(Paid_l)
d=open("PYTHON.txt","r")
s=d.readlines()

#paidcode
m=[i.split("\n") for i in s]#List of resident details

p=[j for i in range(len(m)) for j in m[i] if "Paid" in j]#List of paid users
print()

print("Paid")
for i in p:
    print(i)
print()
'''
d=open("Info.txt","w")
d.write("SRN.No  Flat.no  User Name       Mobile number   UserId   Status\n"
        "01      #001A    SMRITI RANI     9036402304      smr@ST   Paid\n"
        "02      #002A    MS DHONI        8973526345      msd@ST   Paid\n"
        "03      #005B    SHREYA GHOSHAL  2356720984      shre@ST  notpaid\n"
        "04      #021C    GEETA KAPOOR    1775422090      get@ST   Paid\n"
        "05      #005A    VICKY KAUSHAL   9983255178      vick@ST  Paid\n"
        "06      #010B    VIRAT KOHLI     9885462731      vir@ST   notpaid\n"
        "07      #011B    AKSHAY KUMAR    9856554233      aks@ST   Paid\n"
        "08      #009A    SAINA NEHWAL    1265330092      sai@ST   notpaid\n"
        "09      #013B    MARY KOM        9449386440      mar@ST   Paid\n"
        "10      #027C    SHAKTI MOHAN    2445673434      sha@ST   Paid\n"
        "11      #030D    KAMAL HASAN     9880763488      kam@ST   Paid\n"
        "12      #012B    DEEPIKA PADKON  9463527893      deep@ST  Paid\n"
        "13      #022C    ALIA BHAT       3564748376      ali@ST   notpaid\n"
        "14      #011D    RAMESH BABU     6354638977      ram@ST   Paid\n" 
        "15      #018A    RASHMI RAI      5467488948      ras@ST   Paid\n"
        "16      #005C    SAKSHI SINHA    5467876622      sak@ST   Paid\n"
        "17      #015E    K L RAHUL       5610091834      klr@ST   notpaid\n"
        "18      #029B    ANSHUMAN        5468987666      ans@ST   Paid\n"
        "19      #030C    HARSHAL PATEL   3562883667      har@ST   Paid\n"
        "20      #011A    RACHEL ANZITA   4563989899      rac@ST   Paid\n"
        "21      #002B    RAHUL DRAVID    1112453665      rah@ST   not paid\n"
        "22      #101B    SANAM KHAN      2333450987      san@ST   Paid\n"
        "23      #010E    SALMAN KHAN     2567000987      sal@ST   Paid\n"
        "24      #009C    SHREYA PATEL    9449756122      shr@ST   Paid\n"
        "25      #003A    AMITSHA         7022762304      ami@ST   Paid\n"
        "26      #005B    AMITHA SINGH    2346753626      asm@ST   Paid\n"
        "27      #010D    NISHA PATIL     9000943622      nis@ST   notpaid\n"
        "28      #015A    SHAMAN RAJ      1234512345      sha@ST   Paid\n"
        "29      #008C    PREETI ZINTA    9887923043      pre@ST   Paid\n"
        "30      #012B    KAILASH NAYAK   9837378381      kai@ST   Paid\n"
        "31      #041A    SHREYAS IYER    2223456124      shh@ST   notpaid\n"
        "32      #023B    ARJUN KAPOOR    1209128734      arj@ST   Paid\n"
        "33      #041C    BHUMI PEDNEKAR  9875624356      bhu@ST   notpaid\n"
        "34      #011C    ANKIT TIWARI    9449447383      ank@ST   Paid\n"
        "35      #021A    HRITIK ROSHAN   2278534000      hri@ST   Paid\n"
        "36      #032C    KAPIL SHARMA    7227386004      kap@ST   Paid\n"
        "37      #028B    AKSHAY KUMAR    9112565589      aks@ST   Paid\n"
        "38      #034C    ANUSHKA SHARMA  2333245657      anu@ST   Paid\n"
        "39      #020D    PANKAJ TRIPATI  3456728990      pan@ST   notpaid\n"
        "40      #003C    SOURABH JAIN    1289901927      sau@ST   Paid\n"
        "41      #011B    AISHWARYA RAI   9993345600      ais@ST   Paid\n"
        "42      #010B    SACHINTENDULKAR 9043024381      sac@ST   Paid\n"
        "43      #001D    BARAK OBAMA     2229878801      bar@ST   Paid\n"
        "44      #007C    MOHIT SHARMA    2366767234      moh@ST   notpaid\n"
        "45      #026B    DIRUBAI AMABANI 3343098789      dir@ST   Paid\n"
        "46      #011D    KATRINA KAIF    9559386774      kat@ST   notpaid\n"
        "47      #009C    DEEPAK CHAHAR   1127871456      dee@ST   Paid\n"
        "48      #033A    SALMAN KHAN     0909675122      sal@ST   notpaid\n"
        "49      #041C    ANUSHKA SEN     8937466288      sen@ST   notpaid\n"
        "50      #005D    AMITAB BACHAN   7299762304      ami@ST   Paid\n")


d.close()
d=open("Info.txt","r")
s=d.readlines()


m=[i.split("\n") for i in s]#List of resident details

p=[j for i in range(len(m)) for j in m[i] if "Paid" in j]#List of paid users

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
'''
Frame(w,width=600,height=650,bg='lavender').place(x=400,y=30)
k=Label(w,text="Residents who have paid",bg="lavender",fg="Dark blue")
k1=("Lucida Calligraphy",20)
k.config(font=k1)
k.place(x=420,y=70)
j=120
for i in range(len(p)):
    s=Label(w,text=p[i],bg="lavender",fg="Dark red")
   
    s1=("Lucida Calligraphy",7)
    s.config(font=s1)
    s.place(x=430,y=j)
    j+=15
    print(s)
'''

Frame(w,width=600,height=600,bg='lavender').place(x=150,y=20)
k=Label(w,text="Residents who have paid",bg="lavender",fg="Dark blue")
k1=("Lucida Calligraphy",18)
k.config(font=k1)
k.place(x=180,y=40)
j=70
l=len(p)
for i in range((l//2)):
    s=Label(w,text=p[i],bg="lavender",fg="Dark red")
   
    s1=("Lucida Calligraphy",10)
    s.config(font=s1)
    s.place(x=170,y=j)
    j+=30
    print(s)

Frame(w,width=600,height=600,bg='lavender').place(x=670,y=20)
j=80

for i in range((l//2),l+1):
    n=Label(w,text=p[i],bg="lavender",fg="Dark red")
    n1=("Lucida Calligraphy",10)
    n.config(font=n1)
    n.place(x=690,y=j)
    j+=30
    print(n)

w.mainloop()








    
