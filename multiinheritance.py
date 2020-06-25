class Math:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def sum(self):
		return self.x + self.y

class MathExtend1(Math):
	def __init__(sllf, x , y):
		super().__init__(x,y)
    
	def sub(self):
		return self.x - self.y
		
class Extra:
	def division(self, x , y):
		return self.x / self.y

class MathExtend2(MathExtend1, Extra):
	def __init__(self, x, y):
		super().__init__(x,y)

	def multi(self):
		return self.x * self.y

Extend3 = MathExtend2(4,4)
print(" Sum " +str(Extend3.sum()))
print(" Sub "+str(Extend3.sub()))
print(" multi "+str(Extend3.multi()))
print(" Division " +str( Extend3.division(x=Extend3.x, y=Extend3.y)))

        		        
