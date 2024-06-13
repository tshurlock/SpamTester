import detailsVar
import random

class random_person():
    def __init__(self):
        self.first_name = random.choice(detailsVar.firstNames)
        self.surname = random.choice(detailsVar.secondNames)
        self.tel_number = ('07'+ str(random.randint(111111111, 999999999)))
        self.email = (self.first_name +'.' + self.surname +'@' + random.choice(detailsVar.domains)+ '.com')
        self.location = random.choice(detailsVar.locations)
        self.rooms= str(random.randint(1,5))
        self.availability = random.choice(detailsVar.availability)
        self.status = random.choice(detailsVar.status)
        self.day = str(random.randint(1,28))
        self.month = str(random.randint(7,12))
        self.year = '2024'


'''
for testing, can be removed
p1 = random_person()




print('Here is a new person')
print(p1.first_name, p1.surname)
print(p1.email)
print(p1.tel_number)
print(p1.location)
print(p1.rooms)
print(p1.availability)
print(p1.status)
print(p1.day)'''

