from tkinter import *

def click(event):
    global value
    text=event.widget.cget("text")

    if text== "=" :
        if value.get() . isdigit() :
            value1 = int(value.get())
        else :
            value1=eval(display.get())

        value.set(value1)
        display.update()

    elif text == "C" :
        value.set("")
        display.update()

    else :
        value.set(value.get() + text)
        display.update()



root = Tk()
root.geometry("400x550")
root.resizable(False,False)
root.title("Mohit's-Calculator")


root.config(background="silver")

value = StringVar()
value.set("")

display = Entry(root,textvariable=value,font="Comicsansms 30 bold",borderwidth=2,relief=RAISED)
display.pack(fill=X,padx=10,pady=20)

button_frame=Frame(root,background="silver")
button = Button(button_frame,text="9",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button (button_frame,text="8",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="7",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button_frame.place(x=10,y=100)

button_frame=Frame(root,background="silver")
button = Button(button_frame,text="6",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="5",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="4",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button_frame.place(x=10,y=200)

button_frame=Frame(root,background="silver")
button = Button(button_frame,text="3",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="2",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="1",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button_frame.place(x=10,y=300)

button_frame=Frame(root,background="silver")
button = Button(button_frame,text="*",font="Comicsansms 30 bold",padx=8,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="0",font="Comicsansms 30 bold",padx=5,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="/",font="Comicsansms 30 bold",padx=10,pady=2)
button.pack(side=LEFT,padx=10,pady=10)
button.bind("<Button-1>" ,click)
button_frame.place(x=10,y=400)

button_frame=Frame(root,background="gray")
button = Button(button_frame,text="C",font="Comicsansms 30 bold",padx=8,pady=2)
button.pack(padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="+",font="Comicsansms 30 bold",padx=10,pady=2)
button.pack(padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="-",font="Comicsansms 30 bold",padx=15,pady=2)
button.pack(padx=10,pady=10)
button.bind("<Button-1>" ,click)
button = Button(button_frame,text="=",font="Comicsansms 30 bold",padx=10)
button.pack(padx=10,pady=7)
button.bind("<Button-1>" ,click)
button_frame.place(x=280,y=100)

root.mainloop()