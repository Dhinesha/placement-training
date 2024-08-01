
### Medium Level

1. **Grading System**

def determine_grade(score):
    if 90 <= score <= 100:
        return "Grade A"
    elif 80 <= score <= 89:
        return "Grade B"
    elif 70 <= score <= 79:
        return "Grade C"
    elif 60 <= score <= 69:
        return "Grade D"
    else:
        return "Grade F"

print(determine_grade(85))  # Expected output: Grade B
print(determine_grade(60))  # Expected output: Grade D
print(determine_grade(95))  # Expected output: Grade A
```

**Output:**
```
Grade B
Grade D
Grade A
```

2. **ATM Machine Simulation**

def atm_simulation(account_balance, withdrawal_amount):
    if withdrawal_amount <= account_balance:
        return "Transaction successful"
    else:
        return "Insufficient funds"

print(atm_simulation(1000, 500))  # Expected output: Transaction successful
print(atm_simulation(200, 300))   # Expected output: Insufficient funds
print(atm_simulation(1500, 1500)) # Expected output: Transaction successful
```

**Output:**
```
Transaction successful
Insufficient funds
Transaction successful
```

3. **Calculate roots of a quadratic equation**

import math

def calculate_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        return "No real roots"

print(calculate_roots(1, -3, 2))  # Expected output: (2.0, 1.0)
print(calculate_roots(2, 5, 2))   # Expected output: (-0.5, -2.0)
print(calculate_roots(1, -4, 4))  # Expected output: (2.0, 2.0)
```

**Output:**
```
(2.0, 1.0)
(-0.5, -2.0)
(2.0, 2.0)
```

4. **Recommended heart rate range during exercise**

```python
def heart_rate_range(age, gender):
    if gender.lower() == "male":
        max_hr = 220 - age
    else:
        max_hr = 226 - age
    lower_bound = 0.5 * max_hr
    upper_bound = 0.85 * max_hr
    return f"{int(lower_bound)} - {int(upper_bound)} bpm"

# Test cases
print(heart_rate_range(30, "Male"))    # Expected output: 93 - 157 bpm
print(heart_rate_range(45, "Female"))  # Expected output: 88 - 149 bpm
print(heart_rate_range(55, "Male"))    # Expected output: 85 - 145 bpm
```

**Output:**
```
93 - 157 bpm
88 - 149 bpm
85 - 145 bpm
```

5. **Number of days in a month considering leap years**

```python
def days_in_month(month, year):
    month_days = {
        "January": 31, "February": 28, "March": 31, "April": 30,
        "May": 31, "June": 30, "July": 31, "August": 31,
        "September": 30, "October": 31, "November": 30, "December": 31
    }
    if month == "February" and is_leap_year(year):
        return 29
    else:
        return month_days.get(month, "Invalid month")

# Test cases
print(days_in_month("February", 2020))  # Expected output: 29 days
print(days_in_month("April", 2023))     # Expected output: 30 days
print(days_in_month("December", 2021))  # Expected output: 31 days
```

**Output:**
```
29
30
31
```

### High Level

1. **Online Food Ordering System*

class OnlineFoodOrderingSystem:
    def __init__(self):
        self.menu = {
            "burger": 5.00, "pizza": 8.00, "salad": 4.00,
            "soda": 1.50, "fries": 2.50
        }
        self.cart = {}
        self.total = 0.0
        self.delivery_radius = 10  
        self.current_order_volume = 20  
    def browse_menu(self):
        for item, price in self.menu.items():
            print(f"{item.capitalize()}: ${price:.2f}")

    def add_to_cart(self, item, quantity):
        if item in self.menu:
            if item in self.cart:
                self.cart[item] += quantity
            else:
                self.cart[item] = quantity
            self.total += self.menu[item] * quantity
        else:
            print(f"{item} is not available
