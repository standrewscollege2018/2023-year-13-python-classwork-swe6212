from tkinter import *
from tkinter import messagebox 

root = Tk()
root.title("Example of a listbox")
root.geometry('500x400')


############ Functions ##############
def display():
    ''' loop though curselection() to get the indexof the selected list'''
    for i in names_listbox.curselection():
        name.set(f"You have selected{names[i]}")

def add_name():
    ''' add new name to the list'''
    name.append(name_entry.get())
    populate_listbox()

def populate_listbox():
    ''' reload and repopulate the listbox'''
    names_listbox.delete(0,END)
    for name in names:
        names_listbox.insert(END, name)


#List of names to display
names = ["Alan", "Bob", "Charles"]

############# GUI #############
names_listbox = Listbox(root, selectmode=SINGLE)
names_listbox.grid(row=0)



go_button = Button(root, text="Display selection", command=display)
go_button.grid(row=1)

name = StringVar()
name_label = Label(root, testvariable=name)
name_label.grid(row=0, column=1, sticky=S)

name_entry = Entry(root)
name_entry.grid(row=2)
entry_button = Button(root,text="Add name", command=add_name)
entry_button.grid(row=3)

populate_listbox()
root.mainloop()