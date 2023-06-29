# Vectors
This is a test project that allows you to display a graph of an eigenvector on the screen in two lines

# How to use
The initial template with instructions is presented below:

**Please note to take the code from the files render.py and vector.py , they should be located in the same folder as your python executable**
<br>
<br>

## Graph
The graph allows you to display all your work in the form of a beautiful picture
<br>
So far, the graph only allows you to change the size of the cell in pixels

```Python
# setting the cell size to 10 pixels
Graph().setCellSize(10)
```

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

## Motion
Adding movement to the chart

```Python
# importing the space module
from space import *

# importing the render module
from render import *

# the point where the movement started from
start = Location(x = 3, y = 3, z = 3)

# the point where the movement ended
end = Location(x = 6, y = 6, z = 6)

# сreating a movement
# if you do not specify the starting point in the arguments of the class, then by default it will be 0
motion = Motion(end, start)

# creating a new graph
graph = Graph()

# adding a movement to a graph
graph.addMotion(motion)

# launching the graph
graph.run()
```

## Route
### The main functions of the movement

```Python
route = Route()

# rectilinear forward movement of 5 cells / meters
route.forward(5)

# rectilinear back movement of 5 cells / meters
route.back(5)

# rectilinear left movement of 5 cells / meters
route.left(5)

# rectilinear right movement of 5 cells / meters
route.right(5)
```

### Example
making a route
```Python
# importing the space module
from space import *

# importing the render module
from render import *

# creating a new route
route = Route()

# adding to the route that allows you to move to the coordinates (5, 5, 5)
route.addMotion(Motion(Location(x = 5, y = 5, z = 5)))

# adding 4 movements that allow you to visually make a square
route.left(3)
route.forward(3)
route.right(3)
route.back(3)

# creating a new graph
graph = Graph()

# adding a route to a graph
graph.addRoute(route)

# launching the graph
graph.run()
```

https://docs.google.com/presentation/d/1ZkFncAPA1thvLFnxkQJ-X4DiKYDzA_jK/edit?usp=sharing&ouid=109575116193096732086&rtpof=true&sd=true
