from math import *
import rospy
from clover import srv
from std_srvs.srv import Trigger

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

def setMotion(vector: object, speed: int) -> None:
    xDist = vector.x - get_telemetry.x
    zDist = vector.z - get_telemetry.z

    yaw = atan2(zDist, xDist) / pi * 180 - 90
    if (yaw < 0):
        yaw += 360.0

    navigate(x = vector.x, y = vector.y, z = vector.z, speed = int(speed), yaw = yaw)
    rospy.sleep(2)

def lookAt(x: float, z: float) -> None:
    xDist = x - get_telemetry.x
    zDist = z - get_telemetry.z

    yaw = atan2(zDist, xDist) / pi * 180 - 90
    if (yaw < 0):
        yaw += 360.0

    navigate(x = get_telemetry.x, y = get_telemetry.y, z = get_telemetry.z, yaw = yaw)
    rospy.sleep(2)