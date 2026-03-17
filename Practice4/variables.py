
# Known data (2022 statistics provided in practical guidelines):
# - Total population of Scotland: 5,436,600
# - Population of Glasgow: 635,130
# - Population of Edinburgh: 526,470

# 1. Define variables to store population data (integer type)
scotland_pop = 5436600
glasgow_pop = 635130
edinburgh_pop = 526470

# 2. Calculate percentage of population in Glasgow (relative to Scotland)
glasgow_percent = (glasgow_pop / scotland_pop) * 100
# Calculate percentage of population in Edinburgh (relative to Scotland)
edinburgh_percent = (edinburgh_pop / scotland_pop) * 100

# 3. Calculate total population of Glasgow and Edinburgh combined
two_cities_total = glasgow_pop + edinburgh_pop
# Calculate combined percentage of the two cities
two_cities_percent = (two_cities_total / scotland_pop) * 100

# 4. Print results (formatted to 2 decimal places for readability)
print("=== 4.1 Scottish Population Calculation Results ===")
print(f"Total population of Scotland: {scotland_pop:,}")  # Add thousand separators
print(f"Glasgow population percentage: {glasgow_percent:.2f}%")
print(f"Edinburgh population percentage: {edinburgh_percent:.2f}%")
print(f"Total population of Glasgow + Edinburgh: {two_cities_total:,}")
print(f"Combined percentage of two cities: {two_cities_percent:.2f}%")

# ===================== 4.2 Boolean Variables & Truth Table =====================
# 1. Define boolean variables X, Y, W as specified in practical guidelines
X = True
Y = False
W = True

# 2. Print variable values to verify definitions
print("\n=== 4.2 Boolean Variable Definitions ===")
print(f"X = {X}, Y = {Y}, W = {W}")

# 3. Truth table explanation (required for portfolio assessment)
"""
Truth table based on X=True, Y=False, W=True:
1. X and Y → True and False = False
2. X or Y → True or False = True
3. not X → not True = False
4. (X and Y) or W → (False) or True = True
5. X and (Y or W) → True and (False or True) = True
"""

# 4. Verify truth table (optional: execute logical operations for self-check)
print("\n=== Logical Operation Verification ===")
print(f"X and Y = {X and Y}")
print(f"X or Y = {X or Y}")
print(f"not X = {not X}")
print(f"(X and Y) or W = {(X and Y) or W}")
print(f"X and (Y or W) = {X and (Y or W)}")