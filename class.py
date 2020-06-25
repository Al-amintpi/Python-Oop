class Myobject:
	def __init__(self, name, age):
		self.name=name
		self.age=age
	def details(self):
	    print(self.name, self.age, sep="|")	    			    


address = Myobject("alamin", 55)
address.details()

print(address.name, address.age)    

		