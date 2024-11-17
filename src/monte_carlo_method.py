import random


def monte_carlo_pi(n):
    """
    Estimate the value of pi using the Monte Carlo method.

    Parameters:
    - n (int): The number of random points to generate.

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
    
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x*x + y*y <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    pi_approximation = 4 * inside_circle / n
    return pi_approximation, x_inside, y_inside, x_outside, y_outside