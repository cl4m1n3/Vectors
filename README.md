# Vectors
This is a test project that allows you to display a graph of an eigenvector.
<br>
Also, this project supports the control of unmanned aerial vehicles using these vectors
<br>
<br>
functions for operations on vectors:
<br>
**Default**
- addVector(vector: object) - adds another vector to the vector
- subtractVector(vector: object) - subtracts a vector from your vector
- multiply(number: float) - multiplies a vector by a certain number
- divide(number: float) - divides a vector by a certain number
- normalize() - normalizes the vector
- dot(vector: object) - displays a dot
- distance(vector: object) - displays the distance to another vector
- lenght() - displays the length of the vector
<br>
  **Vector2**
- add(x: float, y: float) - adds coordinates to the vector
- subtract(x: float, y: float) - subtracts coordinates from the vector
<br>
  **Vector3**
- add(x: float, y: float, z: float) - adds coordinates to the vector
- subtract(x: float, y: float, z: float) - subtracts coordinates from the vector
- cross(vector: object) - crosses a vector with another vector
- sum(self, *vectors) - sums the set by a vector
- equals(self, vector: object) - returns true if the vector is equal to another vector

# How to use
The initial template with instructions is presented below:
<br>
<br>
Adding a vector to a graph
```Python
from vectors import vector, render

# creating a new vectors
v1 = vector.Vector2(x = 3, y = 3)
v2 = vector.Vector2(x = 2, y = 1)
v3 = vector.Vector2(x = 5, y = 2)

# displaying a graph with vectors that we have created
render.graph(vectors = [v1, v2, v3])
```
<br>
Control of the ROSPY unmanned aerial vehicle

```Python
from vectors import vector
from uav import rospy

# creating a new vector
v = vector.Vector3(x = 5, y = 1, z = 5)

# we set the movement of the UAV using the vector
rospy.setMotion(vector = v)

# this function allows you to make the UAV turn on the spot so that it looks at a certain point along the X and Z coordinates.
rospy.lookAt(x = 5, z = 5)
```
