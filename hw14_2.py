import pickle
from hw14_1 import Employee

with open('mary.pickle', 'rb') as filePickle:
    mary = pickle.load(filePickle)

mary.print_salary_info()
