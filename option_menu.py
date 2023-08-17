#list of names to popular the options menu
names = ['Alan', 'Bob', 'Charles']



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



#start running the program 
root.mainloop()