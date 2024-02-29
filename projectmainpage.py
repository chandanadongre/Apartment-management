from tkinter import *
def x():
    import projectlogin
def y():
    window.destroy()
window =Tk()
#Label(w,text='Prestige Apartment').place(x=0,y=350)

window.geometry("1000x800")
background =PhotoImage(file='./sumukha.gif')
label=Label(window,image=background)
label.place(x=0,y=0)
labelFont =("Academy Engraved LET",36)

labelOne=Label(window,text="Welcome to Sumukha Tropical Apartment")
labelOne.config(font=("Academy Engraved LET",36),bg= "midnight blue", fg= "white")
labelOne.place(x=180,y=100)

labelTwo=Label(window,text='Maintanence Management System')
labelTwo.config(font=labelFont,bg= "deep sky blue", fg= "white")
labelTwo.place(x=180,y=200)

photoToBeLoaded = PhotoImage(file="sumukha.gif")

buttonOne=Button(window,text="Click Here to access Main Menu ",wraplength=200,command=x)
buttonOne.config(font=("Academy Engraved LET",36))
buttonOne.place(x=180,y=350)

buttonTwo=Button(window,text="Click Here to Exit ",wraplength=200,command=y)
buttonTwo.config(font=("Academy Engraved LET",36))
buttonTwo.place(x=180,y=500)

window.mainloop()
