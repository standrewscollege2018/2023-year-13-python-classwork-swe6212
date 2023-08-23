from tkinter import *

############## Functions ###############
def login():
    ''' Get the username and password and check if they are correct'''

    if username.get() == "username" and password.get() == "password":
        # Display success message in console
        print("Success!")
        # Change label to success message and colour to green
        success_message.set("You are now logged in")
        success_label.config(fg='green')
    else:
        print("Wrong!")
        # Example of setting the entry field values back to blank
        username.set("")
        password.set("")
        # Change label to fail message and colour to red
        success_message.set("Incorrect username or password")
        success_label.config(fg='red')
        

############## Create the GUI #################

# Create root window (belongs to Tk class)
root = Tk()
root.title("My first Tkinter GUI")
# Set the size of the window
root.geometry('500x300')
# Prevent users from resizing the window
root.resizable(width=FALSE, height=FALSE)

# Here we are adding labels to the layout, in the left-hand column
user_label = Label(root, text="Username")
user_label.grid(row=0, column=0)

password_label = Label(root, text="Password")
password_label.grid(row=1, column=0)

# Entry fields for username and password go in the second column

# Set variables to store username and password entered
username = StringVar()
password = StringVar()

user_entry = Entry(root, textvariable=username)
user_entry.grid(row=0, column=1)

password_entry = Entry(root, textvariable=password)
password_entry.grid(row=1, column=1)

# Add a login button
# fg is the font colour
login_button = Button(root, text="Login", bg="black", fg="black", command=login)
login_button.grid(row=2, column=0)

# Add a label to display a message after user logs in
success_message = StringVar()
success_message.set("Enter your login details")
success_label = Label(root, textvariable=success_message)
success_label.grid(row=3, column=1)

# run the program
root.mainloop()