#!/usr/bin/python3

def fibonacci_series(n):
    """Returns a list of `n` number of fibonacci sequence"""
    series = [0, 1]

    for i in range (2, n+1):
        x = series[-1] + series[-2]
        series.append(x)
    return series

# sum of first 50 fibonacci sequence
sum_fib = sum(fibonacci_series(50))
print(f"Sum of first 50 fibonacci sequence: {sum_fib}")