import random


def monte_carlo_pi(points_quantity):
    """
    Estimate the value of pi using the Monte Carlo method.

    Parameters:
    - points_quantity (int): The number of random points to generate.

    Returns:
    - pi_approximation (float): The estimated value of pi.
    - x_inside (list): List of x-coordinates of points inside the circle.
    - y_inside (list): List of y-coordinates of points inside the circle.
    - x_outside (list): List of x-coordinates of points outside the circle.
    - y_outside (list): List of y-coordinates of points outside the circle.
    """
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    
    # Generate random points and check if they are inside the circle
    for _ in range(points_quantity):
        x = random.uniform(-1, 1) # Generate random x-coordinate from -1 to 1
        y = random.uniform(-1, 1) # Generate random y-coordinate from -1 to 1
        
        is_inside = x**2 + y**2 <= 1

        inside_circle += is_inside # Increment if the point is inside the circle

        if is_inside:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    
    # formula to calculate the estimated value of pi
    pi_approximation = 4 * inside_circle / points_quantity
    return pi_approximation, x_inside, y_inside, x_outside, y_outside