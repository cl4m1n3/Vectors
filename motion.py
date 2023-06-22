from math import *
import location

class Motion:
    def __init__(self, start_point: object, end_point) -> None:
        self.start_point = start_point
        self.end_point = end_point

    def getStartPoint(self) -> object:
        return self.start_point

    def getEndPoint(self) -> object:
        return self.end_point

    def distance(self) -> float:
        start = self.start_point
        end = self.end_point
        return sqrt(((start.x - end.x) ** 2) + ((start.y - end.y) ** 2) + ((start.z - end.z) ** 2))