''' Student management system '''

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

      #user enters name to search for
    name_search = input("Enter name to search for: ")
    #loop through lists of studentes
    #cheack if the name of a student matches name_search
    #if so, display their details

    for s in students:
      #for an exact match use: if name_search == s.get_name():
      #for a search matching any characters use: if name_search in s.get_name():
        if name_search.lower()+" " in s.get_name().lower() or " " +name_search.lower() in s.get_mame().lower():
            s.display_my_info()

def display_all():
      ''' Display names of all studentds'''

      for s in students:
          s.display_my_info()

def add_student():
    ''' User can add a new student '''

    print("Enter new student details")
    print("-"*20)
    name = input("Name: ")
    #put error catching  around age (use try and exept)
    enter_age = True
    while enter_age:
        try:
            age= int(input("Age: "))
            enter_age = False
        except ValueError:
            print("Enter an integer")
            phone = input("PHone: ")
            student_classes = []
            enter_classes = True
            while enter_class:
                  new_class = input("Class code (end to stop): ")
                  if new_class == "end":
                        #user has finished entering classes
                        enter_class = False
            else: 
                  #add class code to list of classes
                  student_classes.append(new_class)
            #create new student
            Student(name, age, phone, student_classes)
                
add_student()
search()
