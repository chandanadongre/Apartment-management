
'''
d=open("PYTHON.txt","w")
d.write("SRN.No  Flat.no  User Name       Mobile number   UserId   Status\n"
        "01      #001A    SMRITI RANI     9036402304      smr@ST   Paid\n"
        "02      #002A    MS DHONI        8973526345      msd@ST   Paid\n"
        "03      #005B    SHREYA GHOSHAL  2356720984      shre@ST  notpaid\n"
        "04      #021C    GEETA KAPOOR    1775422090      get@ST   paid\n"
        "05      #005A    VICKY KAUSHAL   9983255178      vick@ST  paid\n"
        "06      #010B    VIRAT KOHLI     9885462731      vir@ST   notpaid\n"
        "07      #011B    AKSHAY KUMAR    9856554233      aks@ST   paid\n"
        "08      #009A    SAINA NEHWAL    1265330092      sai@ST   notpaid\n"
        "09      #013B    MARY KOM        9449386440      mar@ST   paid\n"
        "10      #027C    SHAKTI MOHAN    2445673434      sha@ST   paid\n"
        "11      #030D    KAMAL HASAN     9880763488      kam@ST   paid\n"
        "12      #012B    DEEPIKA PADKON  9463527893      deep@ST  paid\n"
        "13      #022C    ALIA BHAT       3564748376      ali@ST   notpaid\n"
        "14      #011D    RAMESH BABU     6354638977      ram@ST   paid\n" 
        "15      #018A    RASHMI RAI      5467488948      ras@ST   paid\n"
        "16      #005C    SAKSHI SINHA    5467876622      sak@ST   paid\n"
        "17      #015E    K L RAHUL       5610091834      klr@ST   notpaid\n"
        "18      #029B    ANSHUMAN        5468987666      ans@ST   paid\n"
        "19      #030C    HARSHAL PATEL   3562883667      har@ST   paid\n"
        "20      #011A    RACHEL ANZITA   4563989899      rac@ST   paid\n"
        "21      #002B    RAHUL DRAVID    1112453665      rah@ST   not paid\n"
        "22      #101B    SANAM KHAN      2333450987      san@ST   paid\n"
        "23      #010E    SALMAN KHAN     2567000987      sal@ST   paid\n"
        "24      #009C    SHREYA PATEL    9449756122      shr@ST   paid\n"
        "25      #003A    AMITSHA         7022762304      ami@ST   paid\n"
        "26      #005B    AMITHA SINGH    2346753626      asm@ST   paid\n"
        "27      #010D    NISHA PATIL     9000943622      nis@ST   notpaid\n"
        "28      #015A    SHAMAN RAJ      1234512345      sha@ST   paid\n"
        "29      #008C    PREETI ZINTA    9887923043      pre@ST   paid\n"
        "30      #012B    KAILASH NAYAK   9837378381      kai@ST   paid\n"
        "31      #041A    SHREYAS IYER    2223456124      shh@ST   notpaid\n"
        "32      #023B    ARJUN KAPOOR    1209128734      arj@ST   paid\n"
        "33      #041C    BHUMI PEDNEKAR  9875624356      bhu@ST   notpaid\n"
        "34      #011C    ANKIT TIWARI    9449447383      ank@ST   paid\n"
        "35      #021A    HRITIK ROSHAN   2278534000      hri@ST   paid\n"
        "36      #032C    KAPIL SHARMA    7227386004      kap@ST   paid\n"
        "37      #028B    AKSHAY KUMAR    9112565589      aks@ST   paid\n"
        "38      #034C    ANUSHKA SHARMA  2333245657      anu@ST   paid\n"
        "39      #020D    PANKAJ TRIPATI  3456728990      pan@ST   notpaid\n"
        "40      #003C    SOURABH JAIN    1289901927      sau@ST   paid\n"
        "41      #011B    AISHWARYA RAI   9993345600      ais@ST   paid\n"
        "42      #010B    SACHINTENDULKAR 9043024381      sac@ST   paid\n"
        "43      #001D    BARAK OBAMA     2229878801      bar@ST   paid\n"
        "44      #007C    MOHIT SHARMA    2366767234      moh@ST   notpaid\n"
        "45      #026B    DIRUBAI AMABANI 3343098789      dir@ST   paid\n"
        "46      #011D    KATRINA KAIF    9559386774      kat@ST   notpaid\n"
        "47      #009C    DEEPAK CHAHAR   1127871456      dee@ST   paid\n"
        "48      #033A    SALMAN KHAN     0909675122      sal@ST   notpaid\n"
        "49      #041C    ANUSHKA SEN     8937466288      sen@ST   notpaid\n"
        "50      #005D    AMITAB BACHAN   7299762304      ami@ST   paid\n")


d.close()
'''
d=open("PYTHON.txt","r")
s=d.readlines()

from tkinter import *
from tkinter import messagebox

w=Tk()
w.geometry('1000x700')
w.title("DATA")
#w.resizable(False,False)

j=0
r=0
for i in range(50):
   c=str(222222+r)
   Frame(w,width=900,height=700,bg='#'+c).place(x=j,y=0)
   j=j+10
   r=r+1

Frame(w,width=600,height=600,bg='lavender').place(x=150,y=20)
k=Label(w,text="Residents details",bg="lavender",fg="Dark blue")
k1=("Lucida Calligraphy",18)
k.config(font=k1)
k.place(x=180,y=40)
j=70
l=len(s)
for i in range((l//2)+1):
    n=Label(w,text=s[i],bg="lavender",fg="Dark red")
    n1=("Lucida Calligraphy",10)
    n.config(font=n1)
    n.place(x=180,y=j)
    j+=20
    print(n)

Frame(w,width=600,height=600,bg='lavender').place(x=670,y=20)
#k=Label(w,text="Residents details",bg="lavender")
#k1=("Lucida Calligraphy",18)
#k.config(font=k1)
#k.place(x=680,y=40)
j=90

for i in range((l//2)+1,l+1):
    n=Label(w,text=s[i],bg="lavender",fg="Dark red")
    n1=("Lucida Calligraphy",10)
    n.config(font=n1)
    n.place(x=690,y=j)
    j+=20
    print(n)

