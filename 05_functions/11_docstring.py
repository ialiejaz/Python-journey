# def my_function():
#     """Demonstrates triple quotes docstring and does nothing."""
#     return None

# print("Using __doc__:")
# print(my_function.__doc__)

# print("Using help():")
# help(my_function)

def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The total area.
    """
    return length * width

print(calculate_area.__doc__)
print(help(calculate_area))