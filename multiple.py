class Person:
	def __init__(self, name, age):
		self.name=name
		self.age=age

	def  details(self):
	     print(self.name, self.age)

person_list = []
for i in range(0,5):
	person = Person("person"+ str(i), 30+i)
	person_list += [person]

for i in person_list:
	i.details()

