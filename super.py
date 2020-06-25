class Math:
	def __init__(self, x, y):
		self.x = x
		self.y =y 

	def sum(self):
		return self.x + self.y


class Mathextend(Math):
	def __init__(self, x, y):
		super().__init__(x, y)

	def subtract(self):
		return self.x - self.y

math_obj = Mathextend(5,2)
print(math_obj.subtract())        
