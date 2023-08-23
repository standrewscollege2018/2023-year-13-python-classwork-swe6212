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

################ Lists to store students, names and classes #############

# lists to store all students
students = []
# Store all student names
student_names = []
# Store all class codes
class_list = []
# List that stores names of students in selected class
student_class_names = []

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
                if line[i] not in class_list:
                    class_list.append(line[i])
                i += 1
            Student(line[0], int(line[1]), line[2], classes)

def display_details():
    ''' Display details of student selected in student_listbox'''

    global student_class_names
    # Start by getting the index of the selected student from the list of names
    for c in student_listbox.curselection():
        selected_student = student_class_names[c]
    # Next we find the matching student and display their info in a label
    for s in students:
        if s.get_name() == selected_student:
            details = f"{'='*30}\nName: {s.get_name()}\nPhone: {s.get_phone()}\nAge: {s.get_age()}\nClasses: {s.get_classes()}\n{'='*30}"
            student_details.set(details)

def populate_student_list(class_code):
    ''' Fill the listbox with students in the selected class '''

    global student_class_names

    # First, delete everything in the listbox
    student_listbox.delete(0, END)

    # create list of student names in selected class
    student_class_names = []
    for s in students:
        if class_code in s.get_classes():
            student_class_names.append(s.get_name())

    # Then populate it with students from selected class
    for s in students:
        if class_code in s.get_classes():
            student_listbox.insert(END, s.get_name())

# Import all students from csv
generate_students()


############ GUI elements ################

# Main window
root = Tk()
root.title("Student Management System")
root.geometry('500x500')  

# Option menu with list of all class codes
selected_class = StringVar()
class_menu = OptionMenu(root, selected_class, *class_list, command=populate_student_list)
selected_class.set(class_list[0])
class_menu.grid(row=0, column=0)


# Listbox with student names
student_listbox = Listbox(root, selectmode=SINGLE)

student_listbox.grid(row=0, column=1)

# Button to get details on selected student
details_button = Button(root, text="Select", command=display_details)
details_button.grid(row=1, column=1)

# Label to display student details
student_details = StringVar()
details_label = Label(root, textvariable=student_details, justify=LEFT)
details_label.grid(row=0, column=2)


# Run program by creating GUI
root.mainloop()