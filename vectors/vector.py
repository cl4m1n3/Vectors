'''
╔╗──╔╗╔═══╗╔═══╗╔════╗╔═══╗╔═══╗╔═══╗
║╚╗╔╝║║╔══╝║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║║╔═╗║
╚╗║║╔╝║╚══╗║║─╚╝╚╝║║╚╝║║─║║║╚═╝║║╚══╗
─║╚╝║─║╔══╝║║─╔╗──║║──║║─║║║╔╗╔╝╚══╗║
─╚╗╔╝─║╚══╗║╚═╝║──║║──║╚═╝║║║║╚╗║╚═╝║
──╚╝──╚═══╝╚═══╝──╚╝──╚═══╝╚╝╚═╝╚═══╝

API-VERSION: 1.1.0

SUPPORTED VERSIONS: 1.0.0
'''
from math import *

class Vector2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector2(x={self.x}y={self.y})"
    
    def add(self, x: float, y: float) -> object:
        return Vector2(self.x + x, self.y + y)
    
    def addVector(self, vector: object) -> object:
        return Vector2(self.x + vector.x, self.y + vector.y)
    
    def subtract(self, x: float, y: float) -> object:
        return Vector2(-x, -y)
    
    def subtractVector(self, vector: object) -> object:
        return self.add(-vector.x, -vector.y)
    
    def multiply(self, number: float) -> object:
        return Vector2(self.x * number, self.y * number)
    
    def divide(self, number: float) -> object:
        return Vector2(self.x / number, self.y / number)
    
    def normalize(self) -> object:
        len = self.x ** 2 + self.y ** 2

        if len > 0:
            return self.divide(sqrt(len))
        
        return Vector2(0, 0)
    
    def dot(self, vector: object) -> float:
        return self.x * vector.x + self.y * vector.y
    
    def distance(self, vector: object) -> float:
        return sqrt((self.x - vector.x) ** 2) + ((self.y - vector.y) ** 2)
    
    def lenght(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)
    
class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"Vector3(x={self.x}y={self.y}z={self.z})"
    
    def add(self, x: float, y: float, z: float) -> object:
        return Vector3(self.x + x, self.y + y, self.z + z)
    
    def addVector(self, vector: object) -> object:
        return Vector3(self.x + vector.x, self.y + vector.y, self.z + vector.z)
    
    def subtract(self, x: float, y: float, z: float) -> object:
        return Vector3(-x, -y, -z)
    
    def subtractVector(self, vector: object) -> object:
        return self.add(-vector.x, -vector.y, vector.z)
    
    def multiply(self, number: float) -> object:
        return Vector3(self.x * number, self.y * number, self.z * number)
    
    def divide(self, number: float) -> object:
        return Vector3(self.x / number, self.y / number, self.z / number)
    
    def cross(self, vector: object) -> object:
        return Vector3(
            self.y * vector.z - self.z * vector.y,
            self.z * vector.x - self.x * vector.z,
            self.x * vector.y - self.y * vector.x
        )
    
    def sum(self, *vectors) -> object:
        x = y = z = 0
        for vector in vectors:
            x += vector.x
            y += vector.y
            z += vector.z

        return Vector3(x, y, z)
    
    def normalize(self) -> object:
        len = self.x ** 2 + self.y ** 2 + self.z ** 2

        if len > 0:
            return self.divide(sqrt(len))
        
        return Vector2(0, 0, 0)
    
    def dot(self, vector: object) -> float:
        return self.x * vector.x + self.y * vector.y
    
    def distance(self, vector: object) -> float:
        return sqrt((self.x - vector.x) ** 2) + ((self.y - vector.y) ** 2)
    
    def lenght(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def equals(self, vector: object) -> bool:
        return self.x == vector.x and self.y == vector.y and self.z == vector.z