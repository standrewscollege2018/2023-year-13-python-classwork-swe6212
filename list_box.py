''' Listbox demonstration '''

from tkinter import *
from tkinter import messagebox

######## Functions #########
def display():
    ''' Loop through curselection() to get the index of the selected item in the listbox'''

    # print(names_listbox.curselection())

    for i in names_listbox.curselection():
        name.set(f"You have selected {names[i]}")

def add_name():
    ''' Add new name to the list '''

    # Popup checks if the user actually wants to enter that name
    if messagebox.askyesno("Double check!", "Are you sure you want to add this name?"):
        names.append(name_to_enter.get())
        populate_listbox()
        # Clear the entry field
        name_to_enter.set("")

def populate_listbox():
    ''' reload and repopulate the listbox '''

    # Clear listbox first
    names_listbox.delete(0,END)
    # Then repopulate
    for name in names:
        names_listbox.insert(END, name)

root = Tk()
root.title("Example of a listbox")
root.geometry('500x400')


# List of names to display
names = ["Alan", "Bob", "Charles"]

######### GUI #########
names_listbox = Listbox(root, selectmode=SINGLE)
names_listbox.grid(row=0)



# Button to display selected name
go_button = Button(root, text="Display selection", command=display)
go_button.grid(row=1)

# Label to display name of selection
name = StringVar()
name_label = Label(root, textvariable=name)
# Using sticky=S to position the label at the bottom of the grid
# Can use N,E,S,W for positioning
name_label.grid(row=0, column=1, sticky=S)

# Entry field and button for adding a new name
name_to_enter = StringVar()
name_entry = Entry(root, textvariable=name_to_enter)
name_entry.grid(row=2)
entry_button = Button(root, text="Add name",  command=add_name)
entry_button.grid(row=3)


populate_listbox()
root.mainloop()