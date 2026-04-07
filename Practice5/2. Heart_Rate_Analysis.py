import numpy as np
import matplotlib.pyplot as plt

heart_rates	=[72,60,126,85,90,59,76,131,88,121,64]
np.append (heart_rates, [55, 130, 78]) # Add new heart rate measurements to the list
#calculate and print the average heart rate from the list of heart rate measurements.
average_heart_rate = np.mean(heart_rates)
print(f"The average heart rate is {average_heart_rate:.2f} bpm.")
# resting heart rate categories: low (<60 bpm), normal (60-120 bpm), and high (>120 bpm). Count the number of patients in each category based on the input list of heart rates and print the results.
resting_heart_rate_categories = {"low": 0, "Normal": 0, "high": 0}
for hr in heart_rates: 
    if hr < 60: 
        resting_heart_rate_categories["low"] += 1
    elif 60 <= hr <= 120: 
        resting_heart_rate_categories["Normal"] += 1
    else: 
        resting_heart_rate_categories["high"] += 1

# print the number of patients in each heart rate category
for category, count in resting_heart_rate_categories.items():
    print(f"{category}: {count} patients")

# create a pie chart to visualize the distribution of patients in each heart rate category using matplotlib. Label the chart with the category names and percentages, and give the chart a title "Resting Heart Rate Categories".
plt.figure(figsize=(8, 8))
plt.pie(resting_heart_rate_categories.values(), labels=resting_heart_rate_categories.keys(), autopct='%1.1f%%')
plt.title('Resting Heart Rate Categories')
plt.show()

