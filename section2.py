#!/usr/bin/env python3
class Second:
    def __init__(ref2obj, name, salary, car):
        ref2obj.name = name
        ref2obj.salary = salary
        ref2obj.car = car
        
    def getname(ref2obj):
        return ref2obj.name
    
    def setname(ref2obj, newname):
        ref2obj.name = newname
        return newname
    
    def salary(ref2obj):
        current = ref2obj.salary
        weekly = int(current)*40
        yearly = int(weekly)*52
        return current, weekly, yearly
        
information = input('Enter a name, salary, fav car: ')
name, salary, favcar = information. split(',')
new1 = Second(name, salary, favcar)
newname = 'anani'
#create an object called obj1 of type First
obj1 = Second(name,salary,favcar)
print('*'*80)
#confirm the membership of the new object
print('obj1 is of type Second:', isinstance(obj1,Second),'\n','*'*80)

#confirm wether the object has attributes and methods
print(dir(obj1),'\n','*'*80)

#confirm attributes and methods available
print(obj1.__dict__,'\n','*'*80)

#print the 2 functions
print('name:',Second.getname(new1),'modified name', Second.setname(new1, newname),'with a salary of (hour,weekly,yearly): ', Second.salary(new1))
