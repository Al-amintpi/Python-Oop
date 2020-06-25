class Mobile:
	def __init__(self, name, model):
		self.name = name
		self.model=model

	def change_name(self, name):
		print(name)

	def details(self, price):
	    print(self.name, self.model, sep="|")
	    print("Phone price" , price)

phone = Mobile('alamin', 330)
phone.details(50000)
# Direct change
phone.name = 'sumsange'
phone.details(677)

#indirect change
phone.change_name('walton')