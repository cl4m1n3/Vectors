# Vectors
This is a test project that allows you to display a graph of an eigenvector on the screen in two lines

# How to use
The initial template with instructions is presented below:

**Please note to take the code from the files render.py and vector.py , they should be located in the same folder as your python executable**
<br>
<br>

## Vector
Adding a vector to a graph
```Python
# importing the vector module
from vector import *

# importing the render module
from render import *


# creating a new vector
vector = Vector2(x = 1, y = 2)

# creating a new graph
graph = Graph()

# adding a vector to a graph
graph.addVector(vector)

# launching the graph
graph.run()
```

## Location
Display of the vector of the direction of view on the object Location
```Python
# importing the space module
from space import *

# importing the render module
from render import *

# creating a new location
location = Location(x = 1, y = 1, z = 1, yaw = 0, pitch = 0)

# the Location class is a point in space, so it cannot be displayed on a graph.
# but it is possible to display the direction of view of this point

# the getDirectionPlane() function returns the correct direction of the object's view in space. 
# but the graph will display it only on the plane
direction = location.getDirectionPlane()

# creating a new graph
graph = Graph()

# adding a view direction vector to a graph
graph.addVector(direction)

# launching the graph
graph.run()
```
<br>
<br>
How to look at a point

```Python
# importing the space module
from space import *

# importing the render module
from render import *

# creating a new location
location = Location(x = 1, y = 1, z = 1, yaw = 0, pitch = 0)

# the point variable is another point.
# but we will use this variable to make the object look at it.
point = Location(x = 5, y = 5, z = 5)

# The lookAt() function forces the object to look at the specified point, thereby changing the vector of the direction of view towards this point
location.lookAt(point)

# getting the direction vector
direction = location.getDirectionPlane()

# creating a new graph
graph = Graph()

# adding a view direction vector to a graph
graph.addVector(direction)

# launching the graph
graph.run()
```
