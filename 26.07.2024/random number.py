import random

def generate_random_number(start, end):
    return random.randint(start, end)

print(f"Random number between 1 and 100: {generate_random_number(1, 100)}")
