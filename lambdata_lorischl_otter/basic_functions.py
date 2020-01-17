# Generate basic functions in order to practice unittesting


def factorial(x):
    """Return the factorial of a given number."""
    if x == 1:
        return 1
    else:
        return factorial(x-1) * x
