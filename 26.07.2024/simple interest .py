def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = input()
rate = input()
time = input()
print(f"Simple Interest: {simple_interest(principal, rate, time)}")
