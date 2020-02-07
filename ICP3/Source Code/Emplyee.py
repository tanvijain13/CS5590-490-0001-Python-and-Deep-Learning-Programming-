# Employee class
class Employee:
    countEmployees = 0
    salaries = []

    #defining default constructor
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        #appending salaries to the list
        Employee.salaries.append(self.salary)
        Employee.countEmployees = self.countEmployees + 1

    #calculating average salary of all employess
    def avg_salary(self, salaries):
        length = len(salaries)
        totalsalary = 0
        for salary in salaries:
            totalsalary = totalsalary + salary
        return totalsalary/length


#Full time Employee class inheriting Employee
class FulltimeEmployee(Employee):
    #redefining the parent class constructor
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

    def testing(self):
        print("subclass test")
#entering data for employees
Employee1 = Employee("Tanvi", "Jain", 750000,"Android")
Employee2 = Employee("sarthak", "jain", 850000,"data analysis")
Employee3 = FulltimeEmployee("thomas", "john", 2000000,"Software developer")
Employee4 = FulltimeEmployee("Ritu", "Jain", 590836,"devops")
Employee5 = Employee("Katie", "winslet", 1734799,"cloud")
print(Employee1.name)
print(Employee2.name)
print(Employee3.name)
print(Employee4.name)
print(Employee5.name)

# Access data member through FulltimeEmployee class
print("Number of Employees: ", FulltimeEmployee.countEmployees)
print("avgsalary: ", Employee1.avg_salary(Employee1.salaries))