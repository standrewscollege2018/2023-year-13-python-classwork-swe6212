'''Student mangement system ''' 

class Student:

    def __init__(self, name):

            # Print Hello
            print("Hello")

            # Assign name to new student
            self._name = name

            # Add the new student to the students list
            students.append(self)

    def get_name(self):
        ''' return the name of the student '''
        return self ._name

# List to store all students 
students = []

# Create student
Student("John Smith")
Student("Joanna Smith")

# Loop thought all students and siaply names
for s in students:
      print(f"Hi my name is {s.get_name()}")