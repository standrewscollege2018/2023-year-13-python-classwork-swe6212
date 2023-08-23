from tkinter import *

######## Functions #########
def double():
    ''' get the value entered in number_entry, double it, and set it to the number variable'''

    value = int(number_entry.get())
    number.set(value*2)


########### GUI creation ############
root = Tk()
root.title("Double it")
root.geometry('400x300')

# Entry field for number
number_entry = Entry(root)
number_entry.grid(row=0)

# Button to call double function
double_button = Button(root, text="Double it!", command=double)
double_button.grid(row=1)

# Double label
number = IntVar()
label = Label(root, textvariable=number)
label.grid(row=2)



# Start program
root.mainloop()