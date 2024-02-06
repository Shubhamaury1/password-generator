from tkinter import*
import random,string

#creating customise window
r=Tk()
r.geometry("500x500")
r.title("PASSWORD GENERATE")

#into text
label=Label(r,text="The Strength of Password")
label.place(x=200,y=20)

def selection():
    selection=choice.get()

choice=IntVar()
R1=Radiobutton(r,text="POOR", variable=choice,value=1,command=selection)
R1.place(x=220,y=50)
R2=Radiobutton(r,text="AVERAGE", variable=choice,value=2,command=selection)
R2.place(x=220,y=80)
R3=Radiobutton(r,text="STRONG", variable=choice,value=3,command=selection)
R3.place(x=220,y=110)
labelchoice=Label(r)

label=Label(r,text="Password Length")
label.place(x=210,y=140)

val=IntVar()
spinlength=Spinbox(r, from_=6,to_=16,text=val,width=17)
spinlength.place(x=200,y=170)


def callback():
    Isum.config(text=passgen())

passgenButton=Button(r,text="Generate Password",bd=5,command=callback,pady=3)
passgenButton.place(x=200,y=200)
password=str(callback)

Isum=Label(r,text="")
Isum.pack(side=BOTTOM)

#logic

poor=string.ascii_uppercase + string.ascii_lowercase
average=string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols="""~!@#$%^&*()_+={}[]:;""<>,.?/"""
strong=poor+average+symbols

def passgen():
    if choice.get()==1:
        return"".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return"".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return"".join(random.sample(strong,val.get()))


label=Label(r,text="Generate Password Is = ")
label.place(x=55,y=480)
r.mainloop()










