from math import *
import vector

class Location(object):

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

        return vector.Vector3(x, y, z).normalize()

    def getDirectionPlane(self) -> object:
        return vector.Vector2(-cos(radians(self.yaw) - pi / 2), -sin(radians(self.yaw) - pi / 2)).normalize()

    def lookAt(self, location: object) -> None:
        horizontal = sqrt((location.x - self.x) ** 2 + (location.z - self.z) ** 2)
        vertical = location.y - self.y

        pitch = -atan2(vertical, horizontal) / pi * 180

        xDist = location.x - self.x
        zDist = location.z - self.z

        yaw = atan2(zDist, xDist) / pi * 180 - 90
        if (yaw < 0):
            yaw += 360.0

        self.yaw = yaw
        self.pitch = pitch

    def setRotation(self, yaw: float, pitch: float) -> None:
        self.yaw = yaw
        self.pitch = pitch