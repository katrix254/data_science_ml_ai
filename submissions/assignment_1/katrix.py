def calculate_rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle given its length and width.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The perimeter of the rectangle.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")
    return 2 * (length + width)

# Example
length = 5
width = 3
perimeter = calculate_rectangle_perimeter(length, width)
print(f"The perimeter of the rectangle is: {perimeter}")
