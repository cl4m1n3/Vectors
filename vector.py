from math import *

class Vector2(object):
	
	def __init__(self, x: float, y: float) -> float:
		self.x = x
		self.y = y

	def getX(self) -> float:
		return self.x
	
	def getY(self) -> float:
		return self.y
	
	def add(self, x: float, y: float) -> object:
		return Vector2(self.x + x, self.y + y)
		
	def addVector(self, vector2: object) -> object:
		return self.add(vector2.x, vector2.y)
	
	def subtract(self, x: float, y: float) -> object:
		return self.add(-x, -y)
	
	def subtractVector(self, vector2: object) -> object:
		return self.subtract(vector2.x, vector2.y)
	
	def abs(self) -> object:
		return Vector2(abs(self.x), abs(self.y))
	
	def multiply(self, number: float) -> object:
		return Vector2(self.x * number, self.y * number)
	
	def divide(self, number: float) -> object:
		return Vector2(self.x / number, self.y / number)
	
	def distance(self, vector: object) -> float:
		return sqrt(self.distanceSquared(vector))
	
	def distanceSquared(self, vector: object) -> float:
		return ((self.x - vector.x) ** 2) + ((self.y - vector.y) ** 2)
	
	def length(self) -> float:
		return sqrt(self.lengthSquared())
	
	def lengthSquared(self) -> float:
		return self.x ** 2 + self.y ** 2
	
	def normalize(self) -> object:
		len = self.lengthSquared()

		if len > 0:
			return self.divide(sqrt(len))
		
		return Vector2(0, 0)
	
	def dot(self, vector: object) -> float:
		return self.x * vector.x + self.y * vector.y
	
	def toString(self):
		return f"Vector2(x=" + str(self.x) + ",y=" + str(self.y) + ")"