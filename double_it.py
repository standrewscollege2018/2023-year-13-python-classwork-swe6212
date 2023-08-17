from tkinter import *

def doube_number():
    x = number.get()
    success_message.set(x*2)

#Creating root window (belongs to tk class)
root = Tk()
root.title("Double It GUI")

#Changing size
root.geometry('500x300')
root.resizable(width=FALSE, height=FALSE)

#defining the function
number = IntVar()
number_entry = Entry(root, textvariable =number)
number_entry.grid(row=2,column=1)

login_button = Button(root, text="Double It", bg="white", fg="black", command=doube_number)
login_button.grid(row=2,column=0)

success_message= StringVar()

success_message.set("Show the doubled number")
success_label = Label(root, textvariable=success_message)
success_label.grid(row = 3, column=1)
 
#Run program
root.mainloop()