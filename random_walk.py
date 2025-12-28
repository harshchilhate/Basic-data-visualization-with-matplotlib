from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points = 5000):
        """Initialize attribute of a walk."""
        self.num_points = num_points

        #All walkes starts at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

        # Explicit movement rules
        self.directions = [1, -1]
        self.distances = [0, 1, 2, 3, 4]


    def fill_walk(self):
        """Calculate all the points in the walk."""
        #Keep taking steps untill the walk reaches the desired length.

        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()

            #Reject moves that go nowhere.
            if (x_step == 0) and (y_step == 0):
                continue

            #calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


    def get_step(self):
            #Decide which direction to go, how far to go
            x_step = choice(self.directions) * choice(self.distances)
            y_step = choice(self.directions) * choice(self.distances)
            return x_step, y_step
    
