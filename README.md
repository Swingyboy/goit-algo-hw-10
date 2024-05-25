# Integral Calculator

This script calculates the integral of the function \( f(x) = e^x \) within a specified range using the Monte Carlo method.

## Usage

Make sure you have Python installed on your system.

1. Clone this repository:
```git clone <repository_url>```
2. Navigate to the repository:
```cd <repository_name>```
3. Run the script with the following command:
```python task_2.py <lower_bound> <upper_bound> <number_of_random_points>```

Example:
```python task_2.py 0 2 100000```


This will calculate the integral of \( f(x) = e^x \) from 0 to 2 using 100000 random points.

## Arguments

- `a`: Lower bound of the integral.
- `b`: Upper bound of the integral.
- `n`: Number of random points to generate for the Monte Carlo method.

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib

## License

This project is licensed under the [MIT License](LICENSE).


This will calculate the integral of \( f(x) = e^x \) from 2 to 5 using 100, 1000, 10000 and 100000000 random points.

## Results

| Number of Random Points | Monte Carlo Method | Analytical Method | Quad Method | MC - Analytical | MC - Quad |
|-------------------------|--------------------|-------------------|-------------|-----------------|-----------|
| 100                     | 120.21             | 141.02            | 141.02      | 20.81           | 20.81     |
| 1000                    | 140.7              | 141.02            | 141.02      | 0.33            | 0.33      |
| 10000                   | 139.09             | 141.02            | 141.02      | 1.93            | 1.93      |
| 100000000               | 141.06             | 141.02            | 141.02      | 0.04            | 0.04      |

## Analysis

The results of the integral calculation using the Monte Carlo method, analytical method, and quad method are summarized in the table above.

- The Monte Carlo method provides an approximation of the integral by randomly sampling points under the curve. As the number of random points increases, the approximation tends to converge to the true value of the integral.

- The analytical method calculates the exact value of the integral using mathematical formulas. It serves as a reference for evaluating the accuracy of the Monte Carlo method.

- The quad method from the SciPy library also computes the integral numerically but uses different algorithms than the Monte Carlo method.

From the results, we can observe that:
- As the number of random points increases, the deviation of the Monte Carlo method from the analytical method decreases, indicating better accuracy.
- The deviation between the Monte Carlo method and the quad method follows a similar trend.

Overall, the Monte Carlo method provides a reasonably accurate approximation of the integral, especially with a large number of random points.
