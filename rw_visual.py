import matplotlib.pyplot as plt 

from random_walk import RandomWalk

#Make a random walk

rw = RandomWalk()
rw.fill_walk()

#Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors = 'none', vmin=0, vmax = rw.num_points)
ax.set_aspect('equal')

#Emphasis the first and last points.
ax.scatter(0, 0, c = 'green', edgecolors='none', s = 100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100 )
plt.show()