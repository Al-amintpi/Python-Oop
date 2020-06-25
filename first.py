class Building():
	def __init__(self, floor, unit, room):
		self.floor= floor
		self.unit=unit
		self.room=room
	def make(self, window, door):
	    self.window = window
	    self.door = door
buildingone=Building(20,50,100)
print(buildingone.make(150,200))
print(buildingone.window)	    


		
		