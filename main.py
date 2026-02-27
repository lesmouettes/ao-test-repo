def greet(name):
    # TODO: add proper greeting with time of day
    return f"Hello, {name}"

def calculate(a, b):
    # TODO: this function crashes if b is 0
    return a / b

if __name__ == "__main__":
    print(greet("World"))
    print(calculate(10, 2))
