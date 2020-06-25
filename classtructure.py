class Student:
	name = ''
	roll = ''
	email = ''
    
	def Computer(self, department):
		print(self.name, self.roll)
		print(department)
	def Food(self, department):
	    print(self.name, self.roll, self.email)
	    print(department)
	def Rac(self, department):
	    print(self.name, self.roll, self.email)
	    print(department)

collage_student = Student()
collage_student.name="alamin"
collage_student.roll=300524
collage_student.email="alamincmt7418@gmail.com"
collage_student.Computer("com")	    
print(type(collage_student))