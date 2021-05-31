import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')
# xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)

def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

# y = m*x + b
# m = (mean(m)*mean(y) - mean(x*y)) / (mean(x))^2 - mean(x^2)
# b = mean(y) - m*mean(x)

def best_fit_line(x, y):
    numerator = (np.mean(x) * np.mean(y) - np.mean(x * y))
    denominator = (np.mean(x) ** 2 - np.mean(x ** 2))
    m = numerator / denominator
    b = np.mean(y) - m * np.mean(x)
    return m, b

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)

# r^2 = 1 - SEy/SE mean(y)

def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [np.mean(ys_orig) for y in ys_orig]
    square_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)

    return 1 - (square_error_regr/squared_error_y_mean)

xs, ys = create_dataset(40, 10, 2, correlation='pos')

m, b = best_fit_line(xs, ys)

regression_line = [(m*x) + b for x in xs]

predict_x = 8
predict_y = (m*predict_x + b)

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.scatter(predict_x, predict_y, s=100, color='green')
plt.show()