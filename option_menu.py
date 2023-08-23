''' Option Menu example '''

# list of names to populate the option menu
names = ['Alan', 'Bob', 'Charles']

######### Functions ##############
def display_selection():
    ''' Display the selected value from the option menu '''

    print(selected_name.get())

def display(second_name):
    ''' Display selected name from second option menu 
    This function is sent the name by the option menu when a selection is made'''

    print(second_name)


############ GUI part ##############

from tkinter import *
root = Tk()
root.title('OptionMenu example')
root.geometry('400x300')

# Option Menu containing list of names
# Set up a variable to store the selected item
selected_name = StringVar()
# Set the initial selection to the first item in the names list
selected_name.set(names[0])
# second parameter is variable storing the selected item
# list populating the menu needs to have an * in front of it
name_menu = OptionMenu(root, selected_name, *names)
name_menu.config(width=20,bg='white', fg='black')
name_menu.grid(row=0)

# Second Option Menu containing list of names
# Set up a variable to store the selected item
selected_name2 = StringVar()
# Set the initial selection to the first item in the names list
selected_name2.set(names[0])
# second parameter is variable storing the selected item
# list populating the menu needs to have an * in front of it
name_menu2 = OptionMenu(root, selected_name2, *names, command=display)
name_menu2.config(width=20,bg='white', fg='black')
name_menu2.grid(row=0, column=1)


# When you press this button, it calls a function that prints the selected value
go_button = Button(root, text="Go", command=display_selection)
go_button.grid(row=2)

# Start running the program
root.mainloop()