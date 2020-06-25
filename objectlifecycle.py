class Person:
	def __init__(self, name):
		self.name = name
		print(self.name + "created")
	def __del__(self):
		print(self.name + "delete")
people = Person("alamin")
people1 = Person("Sajib")

def hello():
   x = Person("X_created")
   y = Person("Y_created")
hello()         		
	
		