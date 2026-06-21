def greet(name):
    # TODO: add proper greeting with time of day
    return f"Hello, {name}"

def calculate(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero: 'b' must be non-zero.")
    return a / b

if __name__ == "__main__":
    print(greet("World"))
    print(calculate(10, 2))
