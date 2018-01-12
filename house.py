#HOUSE OF DEAD 
class HousePark:
	lastname = "박"
	firstname = None
	fullname = None
	
	def __init__(self,_name):
		self.firstname = _name
		self.setName(_name)
	
	def setName(self, _name):
		self.fullname = self.lastname+_name
	
	def travel(self, where):
		print("%s는 %s으로 여행을 갔다.." % (self.fullname, where))	
	
	def love(self, other):
		print("%s와 %s는 사랑에 빠졌다.." % (self.fullname, other.fullname))

	def fight(self, other):
		print("%s와 %s는 싸웠다.." % (self.fullname, other.fullname))

	def __add__(self, other):
		print("%s와 %s는 결혼을 했다.." % (self.fullname, other.fullname))
		
	def __sub__(self, other):
		print("%s와 %s는 이혼했다..." % (self.fullname, other.fullname))		
		
class HouseKim(HousePark):
		
	lastname = "김"
	
	def travel(self, where, day):
		print("%s는 %s으로 %d일 동안 여행을 갔다.." % (self.fullname, where, day))	
		
		
eung = HousePark("응용")
mina = HouseKim("미나")

eung.travel("부산")
mina.travel("부산",3)

eung.love(mina)
eung+mina
eung.fight(mina)
eung-mina
	