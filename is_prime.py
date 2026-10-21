# is_prime.py
# Check whether a whole number entered by the user is prime.

text = input("Enter a whole number: ").strip()
try:
    n = int(text)
except ValueError:
    raise SystemExit(f"Invalid input: {text!r} is not a whole number.")

# Trial division: a prime is above 1 with no divisor d where d * d <= n.
is_prime = n > 1
divisor = 2
while is_prime and divisor * divisor <= n:
    if n % divisor == 0:
        is_prime = False
    divisor += 1

print(f"{n} is prime." if is_prime else f"{n} is not prime.")
