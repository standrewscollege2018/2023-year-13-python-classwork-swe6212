''' Student management system '''

from tkinter import *
from tkinter import messagebox 

################ Define student class #################

class Student:
    ''' Student objects have attributes like name, phone, address, and a list of
    the classes they are enrolled in. There are also getter functions for each,
    as well as functions to display all of their information. '''

    def __init__(self, name, age, phone, classes):
        ''' The init function is called automatically when the object is created'''

         # Assign properties to new student
        # All properties have an underscore in front
        # This means the property is private to the object
        # and they can only be referenced by calling a getter
        # function from the object (encapsulation)
        self._name = name
        self._phone = phone
        self._age = age
        self._classes = classes

        # Student is automatically enrolled
        self._enrolled = True

        # Add the new student to the students list
        students.append(self)
    
    
    def get_name(self):
        ''' Return the name of the student '''

        return self._name
    
    def get_phone(self):
        ''' Return the phone number '''

        return self._phone

    def get_age(self):
        ''' Return their age '''

        return self._age
    
    def get_classes(self):
        ''' Return list of classes they are enrolled in '''

        return self._classes
    
    def get_enrolled(self):
        ''' Return enrolment status '''

        return self._enrolled

    def unenrol(self):
        ''' This is a setter function that changes the value of a property '''

        self._enrolled = False
        
        students.append(self)
        student_names.append(student_names)
################ Lists to store students and their names #################

students = []
student_names = []
classes = ['MAT', 'GRA', 'ENG', 'BIO', 'DTC', 'PHY']


################ Functions #####################

def generate_students():
    ''' Function imports students from csv file '''

    import csv
    with open('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes = []
            i = 3
            while i in range(3,8):
                classes.append(line[i])
                i += 1
            Student(line[0], int(line[1]), line[2], classes)


def populate_listbox():
    ''' reload and repopulate the listbox'''
    #clear list box
    student_listbox.delete(0,END)
    #then repopulate 
    for name in student_names:
        student_listbox.insert(END, name)


################## GUI ###################

# create and configure the main window
root = Tk()
root.title("Demo of oo and Tkinter")
root.geometry('400x400')

classes_menue = StringVar()
selected_class.set(classes[0])
classes_menue = OptionMenu(root, selected_class, *classes, command=filter_students )
classes_menue.grid(row=0)


student_listbox = Listbox(root)
student_listbox.grid(row=0)

#Import students and populate the listbox 
generate_students()
populate_listbox()

#start the program running
root.mainloop()
