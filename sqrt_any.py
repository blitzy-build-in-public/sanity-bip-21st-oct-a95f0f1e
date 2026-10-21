# sqrt_any.py
# Find the square root of any real number; negatives get an imaginary root.
import cmath
import math

text = input("Enter a number: ").strip()
try:
    x = float(text)
except ValueError:
    raise SystemExit(f"Invalid input: {text!r} is not a number.")

# math.sqrt rejects negatives, so cmath supplies their imaginary root.
if x < 0:
    root = cmath.sqrt(x)
else:
    root = math.sqrt(x)

print(f"sqrt({text}) = {root}")
