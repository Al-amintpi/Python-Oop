class Person:
	def __init__(self, name, age, roll):
		self.name = name
		self.age = age
		self.roll = roll
		
	def details(self):
	    print(self.name, self.age, self.roll, sep="|")

person_list = []
for x in range(0,8):
    person = Person("Person "+ str(x), 30+x, 10+x)
    person_list+=[person]

for x in person_list:
    x.details()    


		