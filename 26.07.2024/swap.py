def swap(a, b):
    a, b = b, a
    return a, b

x, y = 5, 10
x, y = swap(x, y)
print(f"Swapped values: x = {x}, y = {y}")
