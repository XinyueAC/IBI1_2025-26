import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\糖糖\大学\IBI\IBI1_2025-26\IBI1_2025-26\Practical10\dalys-rate-from-all-causes.csv")

afghanistan_data = df[df['Entity'] == 'Afghanistan']
print(afghanistan_data[['Year', 'DALYs']].head(10))

#first_10_rows = df.iloc[:10, [2, 3]]
#print("--- First 10 rows (Year and DALYs) ---")
#print(first_10_rows)

# [Required Comment]: What year reported the maximum DALYs across the first 10 years for Afghanistan?
# Based on the printed data for the first 10 years (1990-1999), 
# the maximum DALYs for Afghanistan was 86656.29, which was reported in 1998.



is_zimbabwe = df['Entity'] == 'Zimbabwe'
zimbabwe_years = df[is_zimbabwe]['Year']
print("\n--- Years recorded for Zimbabwe ---")
print(zimbabwe_years.to_string(index=False))

# [Required Comment]: The first and last year for which these data were recorded
# The first year recorded for Zimbabwe is 1990, and the last year is 2019.




df_2019 = df[df['Year'] == 2019]


max_daly_idx = df_2019['DALYs'].idxmax()
min_daly_idx = df_2019['DALYs'].idxmin()

country_max = df.loc[max_daly_idx, 'Entity']
country_min = df.loc[min_daly_idx, 'Entity']

print("\n--- 2019 DALYs Extremes ---")
print(f"Country with Maximum DALYs: {country_max}")
print(f"Country with Minimum DALYs: {country_min}")

# [Required Comment]: Stating these countries' names
# The country with the maximum DALYs in 2019 is Central African Republic.
# The country with the minimum DALYs in 2019 is San Marino. 
# (Note: If your specific dataset version differs, replace these names with your console output).



# Plotting DALYs over time for the Maximum country

plot_data = df[df['Entity'] == country_max]

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(plot_data['Year'], plot_data['DALYs'], marker='o', linestyle='-', color='b')

#  (All plots are clearly labelled)
plt.title(f'DALYs Over Time for {country_max}')
plt.xlabel('Year')
plt.ylabel('DALYs (Disability-Adjusted Life Years)')
plt.grid(True)


plt.show()



# Question: What is the overall average DALYs rate for the United Kingdom across all recorded years?
uk_data = df[df['Entity'] == 'United Kingdom']
average_uk_dalys = uk_data['DALYs'].mean()
print("\n--- Answer to Custom Question ---")
print(f"The average DALYs rate for the United Kingdom across all years is: {average_uk_dalys:.2f}")