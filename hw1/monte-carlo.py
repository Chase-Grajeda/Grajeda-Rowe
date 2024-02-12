# Implements Q8 - Monte Carlo Approximation

import numpy as np
import matplotlib.pyplot as plt

def approximate_pi(num_points: int) -> tuple[float, float]:
    # Generate points    
    points = np.random.uniform(-1,1, size=(num_points,2))
    
    # Retrieve points within circle. Calculate ratio and error (num points within circle / total points)
    circle = [point for point in points if  (point[0] ** 2) + (point[1] ** 2) <= 1]
    approx = 4 * (len(circle) / num_points)
    error = abs(approx - np.pi) / np.pi
    
    return approx, error

if __name__ == "__main__":
    # Monte carlo approximation
    limit = 10_000
    step = 10
    approxs = []
    errors = []
    for num_points in range(step, limit+step, step):
        approx, error = approximate_pi(num_points)
        approxs.append(approx)
        errors.append(error)
    
    # Plot results
    f, (ax1, ax2) = plt.subplots(1,2,figsize=(10,4))
    f.suptitle("Monte Carlo Pi Approximation")
    ax1.plot(approxs)
    ax1.set(xlabel="Num points * 1e2", ylabel="~Pi", title="Approximate Value")
    ax2.plot(errors)
    ax2.set(xlabel="Num points * 1e2", ylabel="Actual vs expected", title="Error")
    
    plt.show()
    