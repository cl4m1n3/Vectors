import rospy
from clover import srv
from std_srvs.srv import Trigger

from space import *

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_altitude = rospy.ServiceProxy('set_altitude', srv.SetAltitude)
set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
set_yaw_rate = rospy.ServiceProxy('set_yaw_rate', srv.SetYawRate)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

class Rospy:

    ''' location : Location '''
    def __init__(self, location: object, name: str):
        self.location = location
        self.name = name
        self.frameid = "body"

        telemetry = get_telemetry(frame_id = self.frameid)
        self.location = Location(telemetry.x, telemetry.y, telemetry.z, telemetry.yaw, telemetry.pitch)

    def getName(self) -> str:
        return self.getName()
    
    def getFrameId(self) -> str:
        return self.frameid
    
    def setFrameId(self, value: str) -> None:
        if value in ("aruco_map" "body", "aruco", "navigate_target", "aruco_N"):
            self.frameid = value
            self.updateLocation()
            return
        
        self.frameid = "body"
        self.updateLocation()

    def getLocation(self) -> object:
        return self.location
    
    ''' location : Location '''
    def setLocation(self, location: object) -> None:
        self.location = location

    def updateLocation(self) -> None:
        telemetry = get_telemetry(frame_id = self.frameid)
        self.location = Location(telemetry.x, telemetry.y, telemetry.z, telemetry.yaw, telemetry.pitch)

    ''' motion : Motion '''
    def setMotion(self, motion: object, speed = 1) -> None:
        start = motion.getStartPoint()
        end = motion.getEndPoint()
        self.location = Location(start.getX(), start.getY(), start.getZ(), start.getYaw(), start.getPitch())

        x = self.location.getX()
        y = self.location.getY()
        z = self.location.getZ()
        yaw = self.location.getYaw()

        navigate(x = x, y = y, z = z, speed = int(speed), yaw = yaw)
        rospy.sleep(1)

        x += end.getX()
        y += end.getY()
        z += end.getZ()
        yaw = (self.location.lookAt(end)).getYaw()

        navigate(x = x, y = y, z = z, speed = int(speed), yaw = yaw)
        rospy.sleep(1)

    ''' vector3 : Vector3 '''
    def setMotionByVector(self, vector3: object, speed = 1) -> None:

        x = self.location.getX() + vector3.getX()
        y = self.location.getY() + vector3.getX()
        z = self.location.getZ() + vector3.getX()
        yaw = (self.location.lookAt(vector3)).getYaw()

        navigate(x = x, y = y, z = z, speed = int(speed), yaw = yaw)
        rospy.sleep(1)

    ''' route : Route '''
    def playRoute(self, route: object) -> None:
        for motion in route.getMotions():
            self.setMotion(motion)