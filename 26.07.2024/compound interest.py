def compound_interest(principal, rate, time):
    return principal * (1 + rate/100) ** time

principal = input()
rate = input()
time = input()
print(f"Compound Interest: {compound_interest(principal, rate, time)}")
