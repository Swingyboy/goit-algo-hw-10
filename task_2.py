import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return np.exp(x)


def x_random(a: float, b: float, n: int) -> np.ndarray:
    return np.random.uniform(a, b, n)


def y_random(b: float, n: int) -> np.ndarray:
    return np.random.uniform(0, np.exp(b), n)


def calculate_area(a: float, b: float) -> float:
    return (b - a) * (np.exp(b))


def calculate_under_curve(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return y <= f(x)


def monte_carlo(a: float, b: float, n: int) -> float:
    x = x_random(a, b, n)
    y = y_random(b, n)
    area_rect = calculate_area(a, b)
    under_curve = calculate_under_curve(x, y)
    monte_carlo_integral = area_rect * np.sum(under_curve) / n
    return monte_carlo_integral


def analytical(a:float, b: float) -> float:
    return np.exp(b) - np.exp(a)


def quad_integration(a: float, b: float) -> float:
    return quad(f, a, b)[0]


def main(a: float, b: float, n: int) -> float:
    monte_carlo_integral = monte_carlo(a, b, n)
    analytical_integral = analytical(a, b)
    quad_integral = quad_integration(a, b)

    print(f"Integral calculated with Monte Carlo method: {round(monte_carlo_integral, 2)}")
    print(f"Integral calculated with analytical method: {round(analytical_integral, 2)}")
    print(f"Integral calculated with quad method: {round(quad_integral, 2)}")

    # Висновок
    print(f"Deviation of the Monte Carlo method from the analytical method:"
          f" {round(abs(monte_carlo_integral - analytical_integral), 2)}")
    print(f"Deviation of the Monte Carlo method from the quad method:"
          f" {round(abs(monte_carlo_integral - quad_integral), 2)}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Calculate the integral of the function f(x) = exp(x) from a to b.')
    parser.add_argument('a', type=float, help='Lower bound of the integral')
    parser.add_argument('b', type=float, help='Upper bound of the integral')
    parser.add_argument('n', type=int, help='Number of random points')
    args = parser.parse_args()
    main(args.a, args.b, args.n)
    plt.show()
