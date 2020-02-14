import pickle


class Employee:
    def __init__(self, name, phone, salary=30000):
        self.name = name
        self.phone = phone
        self.salary = salary

    def print_salary_info(self):
        print("Employee {} gets {} Rubles".format(self.name, self.salary))

    def add_salary(self, delta=5000):
        self.salary = self.salary + delta

    def add(self, other_empl):
        new_name = self.name + "&" + other_empl.name
        new_phone = str(round((int(self.phone) + int(other_empl.phone)) / 2))
        new_salary = self.salary + other_empl.salary
        return Employee(new_name, new_phone, new_salary)

    __add__ = add

    def fire(self):
        print(self.name + " is FIRED!!!")


mary = Employee('Mary', 480062, 80000)
with open('mary.pickle', 'wb') as filePickle:
    pickle.dump(mary, filePickle)