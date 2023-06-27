from math import *
from vector import *

class Location:

    def __init__(self, x: float, y: float, z: float, yaw = float(0), pitch = float(0)) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.yaw = yaw
        self.pitch = pitch

    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y

    def getZ(self) -> float:
        return self.z

    def getYaw(self) -> float:
        return self.yaw

    def getPitch(self) -> float:
        return self.pitch

    def getDirectionVector(self) -> object:
        y = -sin(radians(self.pitch))
        xz = cos(radians(self.pitch))
        x = -xz * sin(radians(self.yaw))
        z = xz * cos(radians(self.yaw))

        return Vector3(x, y, z).normalize()

    def getDirectionPlane(self) -> object:
        return Vector2(-cos(radians(self.yaw) - pi / 2), -sin(radians(self.yaw) - pi / 2)).normalize()

    def lookAt(self, point: object) -> None:
        horizontal = sqrt((point.x - self.x) ** 2 + (point.z - self.z) ** 2)
        vertical = point.y - self.y

        pitch = -atan2(vertical, horizontal) / pi * 180

        xDist = point.x - self.x
        zDist = point.z - self.z

        yaw = atan2(zDist, xDist) / pi * 180 - 90
        if (yaw < 0):
            yaw += 360.0

        self.yaw = yaw
        self.pitch = pitch

    def setRotation(self, yaw: float, pitch: float) -> None:
        self.yaw = yaw
        self.pitch = pitch

class Motion:

    def __init__(self, end_point: object, start_point = Location(0, 0, 0)) -> None:

        # var Vector3 | Location
        self.start_point = start_point
        self.end_point = end_point

    def getStartPoint(self) -> object:
        return self.start_point
    
    def setStartPoint(self, point: object) -> None:
        self.start_point = point

    def getEndPoint(self) -> object:
        return self.end_point
    
    def setEndPoint(self, point: object) -> None:
        self.end_point = point

    def distance(self) -> float:
        start = self.start_point
        end = self.end_point
        return sqrt(((start.x - end.x) ** 2) + ((start.y - end.y) ** 2) + ((start.z - end.z) ** 2))
    
class Route:

    def __init__(self) -> None:
        self.motions = []

    def addMotion(self, motion: object) -> None:
        if len(self.motions) > 0:
            motion.setStartPoint(self.motions[-1].getEndPoint())
            self.motions.append(motion)
            return

        self.motions.append(motion)

    def getMotions(self) -> list:
        return self.motions