import random

def monte_carlo_pi(n):
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