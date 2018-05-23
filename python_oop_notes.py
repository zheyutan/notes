class Employee:

    raise_amont = 1.04
    num_of_emps = 0
    # class variables

    def __init__(self,first,last,pay):
        self.first = first
        self.last= last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps +=1
    # this special dunder method is implicitly called when we create objects 

    # def __repr__(self):
    #     pass
    
    # def __str__(self):
    #     pass

    # print(emp_1)
    # print(emp_1.__repr__())
    def __add__(self,other):
        return self.pay + other.pay

    # print(emp_1 + emp_2)


    def fullname(self):
        return ‘{} {}’。format(self.first,self.last)
    # fullname is a regular methods: automatically take instance as its first arguement

    @classmethod
    def set_raise()_amount(cls,amount):
        cls.raise_amt = amount
    # receive a class as the first argument instead of the instance

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        # self.pay = int(self.pay * raise_amount) 
        self.pay = int(self.pay * Employee.raise_amount)
        # or
        self.pay = int(self.pay * self.raise_amount)
        # we can only access class variables through class itself or instance

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            retrun False
        return True
    # static method does not pass anything automatically, behave just like regular functions 
    # except we include them in the classes because they have some logic connection with the class

    

emp_1 = Employee('jo','tan',5000)
emp_2 = Employee('wei','jiang',4999)

emp_str_1 = 'john-doe-7000'
emp_str_1 = 'steve-smith-6000'
emp_str_1 = 'jane-doe-3000'
first,last,pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last,pay)
# create instance from strings, see classmethod: from string above

# *****Inheritance
# python walk upu this chain(resolution order) of Inheritance 
class Developer(Employee):
    raise_amount = 1.10

def __init__(self,first,last,pay,prog_lang):
    super().__init__(first,last,pay)
    # maintainable,let class Employedd hand first three variables
    self.prog_lang = prog_lang

dev_1 = Developer('jo','tan',5000,'python')
dev_2 = Developer('wei','jiang',4999,'java')
help(Developer)



class Manager(Employee):
    raise_amount = 1.10

def __init__(self,first,last,pay,employees=None):
    super().__init__(first,last,pay)
    # maintainable,let class Employedd hand first three variables
    if self.employees is None:
        self.employees = []
    else:
        self.employees = employees

def add_emp(self,emp):
    if emp not in self.employees:
        self.employees.append(emp)

def remove_emp(self,emp):
    if emp in self.employees:
        self.employees.remove(emp)
def print_emp(self):
    for emo in self.employees:
        print('-->',emp.fullname())




# two build-in function:isinstance and issubclass
print(isinstance(dev1,Employee))
# True
print(issubclass(Manager,Employee))
# True
# subclassing example: exception module of this Python whisky llibrary

# print(1+2)
# print(int.__add__(1,2))

# property decotators allows us to define a method but we can access it like an attribute
# @property
# @setter
#@deleter