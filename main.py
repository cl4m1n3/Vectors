import vector
import location
import render
import motion
from math import *

start = location.Location(2, 2, 0, -90, -45)
end = location.Location(5, 5, 0, 45, 0)

gr = render.Graph()
gr.addMotion(motion.Motion(start, end))
gr.run()