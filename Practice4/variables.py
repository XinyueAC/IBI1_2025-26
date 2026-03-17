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
    # Population growth rate remains unchanged between the two decades.

   # Answer to the question: Is population growth accelerating or decelerating?
   #decellerating, because the increase in population from 2014 to 2024 (0.22 million) is smaller than the increase from 2004 to 2014 (0.25 million).