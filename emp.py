class Employee:

    emp_count = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

        Employee.emp_count +=1

    def display_emp_count(self):
        print(f"Total number of employees(s) is (Employee.emp_count)")

    def display_employee(self):
        print("Name: ", self.name, "Salary: ",self.salary)

    def modify_tasks(self, name, status,task):
        self.task = {name: task}



emp1 = Employee("Mihai",50)
emp2 = Employee("Vali",4000)

emp1.display_emp_count()