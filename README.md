# Vectors
This is a test project that allows you to display a graph of an eigenvector.
<br>
A vector can be created in one line of code
<br>
Also, this project supports the control of unmanned aerial vehicles using these vectors

# How to use
The initial template with instructions is presented below:
<br>
<br>
Adding a vector to a graph
```Python
from vectors import vector, render

# creating a new vectors
v1 = vector.Vector2(3, 3)
v2 = vector.Vector2(2, 1)
v3 = vector.Vector2(5, 2)

# displaying a graph with vectors that we have created
render.graph([v1, v2, v3])
```
