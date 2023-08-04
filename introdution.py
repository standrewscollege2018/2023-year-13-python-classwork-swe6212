'''Student mangement system ''' 

class Student:

    def __init__(self, name, age, phone, classes):

            # Print Hello
            print("Hello")

            # Assign name to new student
            # All properties have an underscore in front 
            # This means the property is prive to the object
            # And they can only be referenced by calling a getter 
            # Function from the object (encapsulation)
            self._name = name
            self._age = age
            self._phone = phone
            self._classes = classes 

            # Student is automatically enrolled 
            self._enrol = True 

            # Add the new student to the students list
            students.append(self)


    def get_name(self):
        ''' return the name of the student '''
        return self._name
    
    def get_age(self):
          ''' return the age of the student'''
          return self._age
    
    def get_phone(self):
          ''' return the phone number of the student '''
          return self._phone
    
    def get_classes(self):
          ''' return the classes of the student'''
          return self._classes
    
    def get_enrol(self):
          ''' return the enrol of the students'''
          return self._enrol
    
    def unenrol(self):
        ''' this is a setter funtion that changes the value of a '''

        self._enrol = False

        
        def display_my_info(self):
              ''' this displays all infoamtion about the student '''
              print("=" * 30)
              print(f"Name: {self._name}")
              print(f"Age: {self._age}")
              print(f"phone: {self._phone}")
              print(f"classes:", end=" ")
              for c in self._classes:
                        print(c, end = " ")
                        print()
              print("=" * 30)

# List to store all students 
students = []

# Create student
Student("John Smith", 18, "021 123 987", ["DIGI", "MATH"])
Student("Joanna Smith", 17, "027 987 123", ["SIENC", "ECO"])

def search():
      ''' user searches for student'''
      name_search = input("Enter name to search for: ")