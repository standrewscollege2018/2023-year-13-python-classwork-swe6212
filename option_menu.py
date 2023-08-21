#list of names to popular the options menu
names = ['Alan', 'Bob', 'Charles']

def display_selection():
    ''' display selected value from second option menu'''
    print(selected_name.get())

def display(n):
    ''' display selected name from second option menu'''
    print(n)

################ GUI start #############
from tkinter import *

root = Tk()
root.title('Option Menue Example')
root.geometry('1080x1080')

#option menu containg list of names 
#set up a variable to store the selected iteam
selected_name = StringVar()
selected_name.set(names[0])
#second parmter is varable strong the selected iteam 
#list populating the menue needs to have an * in front of it 




name_menu = OptionMenu(root, selected_name, *names)
#name_menu.config(bg='#1234',fg='white')
name_menu.grid(row=0)

#when you press the botton 
go_button = Button(root, text="Go", command=display_selection)
go_button.grid(row=2)

selected_name2 = StringVar()
selected_name2.set(names[0])

name_menu2 = OptionMenu(root, selected_name2, *names, command=display)
#name_menu.config(bg='#1234',fg='white')
name_menu2.grid(row=0, column=1)



#start running the program 
root.mainloop()