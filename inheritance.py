class Math:
	def __init__(self, x, y):
		self.x = x 
		self.y = y

	def sum(self):
	    return self.x + self.y

class Child(Math):
	def __init__(self, x, y):
		super().__init__(x, y)

	def sub(self):
	    return self.x - self.y

man = Child(5,3)
print(man.sub())  	
