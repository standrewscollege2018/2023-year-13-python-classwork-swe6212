''' Student management system '''

class Student:
    ''' Student objects have attributes like name, phone, address, and a list of
    the classes they are enrolled in. There are also getter functions for each,
    as well as functions to display all of their information. '''

    def __init__(self, name, age, phone, classes):
        ''' The init function is called automatically when the object is created'''

        print("Hello")

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

# list to store all students
students = []

# Create students
Student("John Smith", 18, "027123123", ["DIGI", "MATH"])
Student("Joanna Smith", 17, "021321321", ["DIGI", "BIOL"])

def search():
    ''' User searches for student '''

    name_search = input("Enter name to search for: ")
    