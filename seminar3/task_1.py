# 1) Переписать код в соответствии с Single Responsibility Principle:


class Employee():
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

# Подсказка: вынесите метод calculateNetSalary() в отдельный класс


class Count:
    def __init__(self):
        self.base_salary = None

    def calculate_net_salary(self):
        tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
        return self.base_salary - tax
