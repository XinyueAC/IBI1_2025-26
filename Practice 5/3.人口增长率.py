import numpy as np
import matplotlib.pyplot as plt

#2020年和2024年5个国家人口数据表格
population_data = {
    "Country": ["UK", "China", "Italy", "Brazil", "USA"],
    "Population_2020": [66.7, 1426, 59.4, 208.6, 331.6],  # 单位：million
    "Population_2024": [69.2, 1410, 58.9, 212.0, 340.1]   # 单位：million
}
countries = population_data["Country"]
population_2020 = population_data["Population_2020"]
population_2024 = population_data["Population_2024"]
#calculate and print the percentage change of each population using the below equetion: percentage_change = ((population_2024 - population_2020) / population_2020) * 100
percentage_change = ((np.array(population_2024) - np.array(population_2020)) / np.array(population_2020)) * 100
for country, change in zip(countries, percentage_change):
    print(f"{country}: {change:.2f}%")
#Print the population changes in descending order,fromthe largest increase to the largest decrease.Identify which country has the largest increase and which country has the largest decrease in population.
sorted_indices = np.argsort(percentage_change)[::-1]
print("\nPopulation changes in descending order:")
for i in sorted_indices:
    print(f"{countries[i]}: {percentage_change[i]:.2f}%")
largest_increase_country = countries[sorted_indices[0]]
largest_decrease_country = countries[sorted_indices[-1]]
print(f"\nCountry with the largest increase: {largest_increase_country}")
print(f"Country with the largest decrease: {largest_decrease_country}")
#创建一个带有标签的条形图，显示每个国家的人口变化。
plt.figure(figsize=(10, 6))
plt.bar(countries, percentage_change, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Country')
plt.ylabel('Percentage Change in Population (%)')
plt.title('Population Change from 2020 to 2024')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

