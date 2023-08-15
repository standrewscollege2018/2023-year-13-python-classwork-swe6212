from tkinter import *

############ Funchtions ##################
def login():
    ''' Get the username and password and cheack if they are correct'''

    if username.get()== "username" and password.get() == "password":
        #dispaly success message 
        print("Success!")
        success_message.set("You are now logged in")
        success_message.config(fg= "green")
    else:
        print("Wrong!")
        #if username is wrong it resets the feild 
        username.set("")
        password.set("")


############ Create the GUI ###############

#create root window (belongs to Tk class)
root = Tk()
root.title("My frist Tkinter GUI")
#set the size of the window 
root.geometry('500x300')
#prevent the user to resize the window (FALUSE)
root.resizable(width=FALSE, height=FALSE)

#here is an example of a label
user_label = Label(root, text="Username")
user_label.grid(row=0, column=0)

password_label = Label(root, text="password")
password_label.grid(row=1, column=0)

#Eentry fields for username and password go in the second column

#set variables to store username and passsword entered 
username = StringVar()
password = StringVar()

user_entry = Entry(root, textvariable=username)
user_entry.grid(row=0, column=1)

password_entry = Entry(root, textvariable=password)
password_entry.grid(row=1, column=1)

#add a login button 
#fg is the font colour
login_button = Button(root, text="login", bg="black", fg="white", command=login)
login_button.grid(row=2, column=0)

#add a label to display a message after user login
success_message = StringVar()
success_message.set("Enter your login details")
success_label = Label(root, textvariable=success_message)
success_label .grid(row=3, column=1)

#run the program 
root.mainloop()