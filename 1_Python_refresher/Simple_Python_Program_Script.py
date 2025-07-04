# Circle Calculator

"""Python program to calculate area and circumference of a circle """

# 1. Import necessary modules
# Import any libraries or modules your program requires.
import math

# 2. Define constants
# Define fixed values to be used throughout the program.
PI = 3.14159

# 3. Define classes
# Classes are used to model real-world entities or concepts, encapsulating data and behavior.
class Circle:
    """A class to represent a circle."""
    
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def calculate_area(self):
        """Calculate the area of the circle."""
        return PI * self.radius ** 2

    def calculate_circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * PI * self.radius

# 4. Define other functions
# Additional functions can be defined outside of the class for specific tasks.
def greet_user():
    """Greet the user."""
    print("Welcome to the Circle Calculator!")

# 5. Main program execution
# The main logic of the program is placed here.
if __name__ == "__main__":
    # Greet the user
    greet_user()

    # Get user input
    radius = float(input("Enter the radius of the circle: "))
    
    # Create a Circle object
    circle = Circle(radius)
    
    # Perform calculations
    area = circle.calculate_area()
    circumference = circle.calculate_circumference()
    
    # Display results
    print(f"The area of the circle is: {area}")
    print(f"The circumference of the circle is: {circumference}")