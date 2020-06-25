class Person:
	def __init__(self, x , y):
		self.x = x 
		self.y = y
	def sum(self):
	  return self.x + self.y

class MathExtend(Person):
    def __init__(self, x, y):
        super().__init__(x, y)	

    def sub(self):
      return self.x - self.y

    def sum(self): #Method override
      return self.x + self.y +100

    def showall(self):
    	print("super" +str(super().sum()))
    	print("sum" +str(self.sum()))
		print('sub' +str(self.sub()))  

Extend2 = MathExtend(10,2)
Extend2.showall()   


