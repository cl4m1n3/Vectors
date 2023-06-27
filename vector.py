from math import *

class Vector2:

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

class Vector3:

    def __init__(self, x: float, y: float, z: float) -> float:
        self.x = x
        self.y = y
        self.z = z

    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y

    def getZ(self) -> float:
        return self.z

    def add(self, x: float, y: float, z: float) -> object:
        return Vector3(self.x + x, self.y + y, self.z + z)

    def addVector(self, vector3: object) -> object:
        return self.add(vector3.x, vector3.y, vector3.z)

    def subtract(self, x: float, y: float, z: float) -> object:
        return self.add(-x, -y, -z)

    def subtractVector(self, vector3: object) -> object:
        return self.subtract(vector3.x, vector3.y, vector3.z)

    def abs(self) -> object:
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def multiply(self, number: float) -> object:
        return Vector3(self.x * number, self.y * number, self.z * number)

    def divide(self, number: float) -> object:
        return Vector3(self.x / number, self.y / number, self.z / number)

    def distance(self, vector: object) -> float:
        return sqrt(self.distanceSquared(vector))

    def distanceSquared(self, vector: object) -> float:
        return ((self.x - vector.x) ** 2) + ((self.y - vector.y) ** 2) + ((self.z - vector.z) ** 2)

    def length(self) -> float:
        return sqrt(self.lengthSquared())

    def lengthSquared(self) -> float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalize(self) -> object:
        len = self.lengthSquared()

        if len > 0:
            return self.divide(sqrt(len))

        return Vector3(0, 0, 0)

    def dot(self, vector: object) -> float:
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def toString(self) -> str:
        return f"Vector3(x=" + str(self.x) + ",y=" + str(self.y) + ",z=" + str(self.z) + ")"