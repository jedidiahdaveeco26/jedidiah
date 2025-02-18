class Employee:
    def __init__(self, name, position, salary):
        # Initialize employee attributes
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        # Method to increase the salary
        self.salary += amount

    def display_employee(self):
        # Method to display employee details
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

# Create an employee instance
employee1 = Employee("Jedidiah", "computer engineer", 4500)

# Display initial employee details
print("Before raise:")
employee1.display_employee()

# Give the employee a raise
employee1.give_raise(4500)
# Display employee details after the raise
print("\nAfter raise:")
employee1.display_employee()