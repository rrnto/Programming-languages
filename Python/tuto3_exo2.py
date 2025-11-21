## Define a Star class with attributes for position, magnitude, and spectral type
class Star:
    def __init__(self, position_x, position_y, magnitude, spectral_type):
        self.position_x = position_x
        self.position_y = position_y
        self.magnitude = magnitude
        self.spectral_type = spectral_type
    
    def display_info(self):
        print(f"Position: ({self.position_x}, {self.position_y}), Magnitude: {self.magnitude}, Spectral Type: {self.spectral_type}")

my_star = Star(10, 20, -1.5, 'G-type')
my_star.display_info() 


## Expanding the Star class:
# a) Create 10 Star objects and display their information:
stars = [
    Star(1, 2, 1.1, 'O'), Star(2, 3, 1.5, 'B'), Star(3, 4, 2.0, 'A'),
    Star(4, 5, 2.5, 'F'), Star(5, 6, 3.0, 'G'), Star(6, 7, 3.5, 'K'),
    Star(7, 8, 4.0, 'M'), Star(8, 9, 4.5, 'L'), Star(9, 10, 5.0, 'T'),
    Star(10, 11, 5.5, 'Y'), Star(0, 0, -2, 'O'), Star(1, 1, 4, 'G')
]

for star in stars:
    star.display_info() 


# b) Add a method to compute the distance between two stars:
import math

def distance_to(self, other_star):
        distance = math.sqrt((self.position_x - other_star.position_x) ** 2 +
                             (self.position_y - other_star.position_y) ** 2)
        return distance

Star.distance_to = distance_to

star1 = stars[0]
star2 = stars[2]
print(f"Distance between star1 and star2: {star1.distance_to(star2)}") 
