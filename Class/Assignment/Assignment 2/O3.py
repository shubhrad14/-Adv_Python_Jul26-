# Base Class
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def calculate_salary(self):
        pass


# Derived Class - Full Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Derived Class - Part Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hours_worked, hourly_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


# Derived Class - Contract Employee
class ContractEmployee(Employee):
    def __init__(self, employee_id, name, project_amount, bonus):
        super().__init__(employee_id, name)
        self.project_amount = project_amount
        self.bonus = bonus

    def calculate_salary(self):
        return self.project_amount + self.bonus


# Payroll Class
class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def generate_payroll(self):
        total_payroll = 0

        for emp in self.employees:
            salary = emp.calculate_salary()   # Polymorphism
            print("Employee ID :", emp.employee_id)
            print("Name :", emp.name)
            print("Salary : ₹", salary)
            print()

            total_payroll += salary

        print("Total Payroll = ₹", total_payroll)


# Test Data
emp1 = FullTimeEmployee("E101", "Anand", 60000)
emp2 = PartTimeEmployee("E102", "Iksha", 120, 150)
emp3 = ContractEmployee("E103", "Chinmayi", 45000, 5000)

payroll = Payroll()

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

payroll.generate_payroll()