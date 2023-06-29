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

    def setX(self, value: float) -> object:
        return Location(value, self.y, self.z)

    def getY(self) -> float:
        return self.y

    def setY(self, value: float) -> object:
        return Location(self.x, value, self.z)

    def getZ(self) -> float:
        return self.z

    def setZ(self, value: float) -> object:
        return Location(self.x, self.y, value)

    def getYaw(self) -> float:
        return self.yaw

    def setYaw(self, value: float) -> None:
        return Location(self.x, self.y, self.z, value, self.pitch)

    def setPicth(self, value: float) -> None:
        return Location(self.x, self.y, self.z, self.yaw, value)

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
    
    ''' point : Location|Vector3 '''
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

    ''' end_point : Location|Vector3 '''
    def __init__(self, end_point: object, start_point = Location(0, 0, 0)) -> None:

        self.start_point = start_point
        self.end_point = end_point

    def getStartPoint(self) -> object:
        return self.start_point

    ''' point : Location|Vector3 '''
    def setStartPoint(self, point: object) -> None:
        self.start_point = point

    def getEndPoint(self) -> object:
        return self.end_point
    
    ''' point : Location|Vector3 '''
    def setEndPoint(self, point: object) -> None:
        self.end_point = point

    def distance(self) -> float:
        start = self.start_point
        end = self.end_point
        return sqrt(((start.x - end.x) ** 2) + ((start.y - end.y) ** 2) + ((start.z - end.z) ** 2))

class Route:

    def __init__(self) -> None:
        self.motions = []

    ''' motion : Motion '''
    def addMotion(self, motion: object) -> None:
        if len(self.motions) > 0:
            motion.setStartPoint(self.motions[-1].getEndPoint())
            self.motions.append(motion)
            return

        self.motions.append(motion)

    def getMotions(self) -> list:
        return self.motions

    def left(self, distance: float) -> None:
        if len(self.motions) > 0:
            motion = self.motions[-1]
            m = Motion(Location(0, 0, 0))
            m.setStartPoint(motion.getEndPoint())
            m.setEndPoint(m.getStartPoint().setX(m.getStartPoint().getX() - distance))
            self.motions.append(m)
            return

        self.motions.append(Motion(Location(0 - distance, 0, 0)))

    def right(self, distance: float) -> None:
        if len(self.motions) > 0:
            motion = self.motions[-1]
            m = Motion(Location(0, 0, 0))
            m.setStartPoint(motion.getEndPoint())
            m.setEndPoint(m.getStartPoint().setX(m.getStartPoint().getX() + distance))
            self.motions.append(m)
            return

        self.motions.append(Motion(Location(distance, 0, 0)))

    def forward(self, distance: float) -> None:
        if len(self.motions) > 0:
            motion = self.motions[-1]
            m = Motion(Location(0, 0, 0))
            m.setStartPoint(motion.getEndPoint())
            m.setEndPoint(m.getStartPoint().setY(m.getStartPoint().getY() + distance))
            self.motions.append(m)
            return

        self.motions.append(Motion(Location(0, distance, 0)))

    def back(self, distance: float) -> None:
        if len(self.motions) > 0:
            motion = self.motions[-1]
            m = Motion(Location(0, 0, 0))
            m.setStartPoint(motion.getEndPoint())
            m.setEndPoint(m.getStartPoint().setY(m.getStartPoint().getY() - distance))
            self.motions.append(m)
            return

        self.motions.append(Motion(Location(0, 0 - distance, 0)))