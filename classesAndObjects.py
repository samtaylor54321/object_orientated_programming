class Employee:
    # Define an attribute called name
    name = "Ben"

    def changeName (self):
        # Change the value of the attribute within a method
        Employee.name = "Mark"

employee = Employee()
print(employee.name)
employee.changeName()
print(employee.name)
