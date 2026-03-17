# Store Scottish population data (in millions) for different years
# 2004 population: 5.08 million
a = 5.08
# 2014 population: 5.33 million
b = 5.33
# 2024 population: 5.55 million
c = 5.55

# Calculate population change between 2004 and 2014 (b - a)
d = b - a
# Calculate population change between 2014 and 2024 (c - b)
e = c - b

# Print results for verification

print(f"2004 population (a): {a} million")
print(f"2014 population (b): {b} million")
print(f"2024 population (c): {c} million")
print(f"Population change 2004-2014 (d = b - a): {d} million")
print(f"Population change 2014-2024 (e = c - b): {e} million")

# Compare d and e, and comment on population growth trend

if d > e:
    print(f"d ({d} million) is larger than e ({e} million).")
 
    # Population growth is decelerating, as the absolute increase in population is smaller in the later decade.
elif e > d:
    print(f"e ({e} million) is larger than d ({d} million).")
    # Population growth is accelerating, as the absolute increase in population is larger in the later decade.
else:
    print(f"d ({d} million) and e ({e} million) are equal.")
    # Population growth rate remains unchanged between the two decade

    # Task: Compare d and e. Determine if growth is accelerating or decelerating
# Record your answer as a comment below
# Answer: Since d (0.25 million) is larger than e (0.22 million), the population growth is decelerating in Scotland.

# ===================== 4.2 Booleans =====================
# Task 1: Create variables X and Y (X = True, Y = False)
X = True
Y = False

# Task 2: Create variable W which encodes "X or Y"
W = X or Y

# Print Boolean values for verification
print("\n=== 4.2 Boolean Variables ===")
print(f"X = {X}, Y = {Y}")
print(f"W = X or Y = {W}")