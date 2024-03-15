def determine_triangle_type(x, y, z):
    """
    Determine the type of triangle based on the input sides.

    Args:
    x (int): Length of the first side.
    y (int): Length of the second side.
    z (int): Length of the third side.

    Returns:
    str: A string indicating the type of triangle.

    Raises:
    ValueError: If any side length is non-positive.
    """

    if x <= 0 or y <= 0 or z <= 0:
        raise ValueError("Triangle sides must be positive integers")

    if x == y == z:
        return "Equilateral triangle"
    elif x == y or x == z or y == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

x = int(input("Enter the length of the first side: "))
y = int(input("Enter the length of the second side: "))
z = int(input("Enter the length of the third side: "))

try:
    result = determine_triangle_type(x, y, z)
    print(f"The triangle is a {result}.")
except ValueError as e:
    print(f"Error: {e}")
