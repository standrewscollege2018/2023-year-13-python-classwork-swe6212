''' Student management system with GUI '''

from tkinter import *

############### Class definition for Student ###################

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

        # Add the new student to the students list and name to student_names list
        students.append(self)
        student_names.append(self._name)
    
    
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

    def display_my_info(self):
        ''' This displays all information about the student '''

        print("=" * 30)
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Phone: {self._phone}")
        # Display all classes on one line
        print(f"Classes: ", end=" ")
        for c in self._classes:
            print(c, end=" ")
        print()
        print("=" * 30)

# lists to store all students and names
students = []
student_names = []


########### Functions ###################

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

def display_details():
    ''' Display details of student selected in student_listbox'''

    # Start by getting the index of the selected student from the list of names
    for c in student_listbox.curselection():
        selected_student = student_names[c]
    # Next we find the matching student and display their info in a label
    for s in students:
        if s.get_name() == selected_student:
            details = f"{'='*30}\nName: {s.get_name()}\nPhone: {s.get_phone()}\nAge: {s.get_age()}\nClasses: {s.get_classes()}\n{'='*30}"
            student_details.set(details)



# Import all students from csv
generate_students()


############ GUI elements ################

# Main window
root = Tk()
root.title("Student Management System")
root.geometry('500x500')  

# Listbox with student names
student_listbox = Listbox(root, selectmode=SINGLE)
for name in student_names:
    student_listbox.insert(END, name)
student_listbox.grid(row=0, column=0)

# Button to get details on selected student
details_button = Button(root, text="Select", command=display_details)
details_button.grid(row=1, column=0)

# Label to display student details
student_details = StringVar()
details_label = Label(root, textvariable=student_details, justify=LEFT)
details_label.grid(row=0, column=1)


# Run program by creating GUI
root.mainloop()