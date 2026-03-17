import numpy as np
import matplotlib.pyplot as plt

heart_rates	=[72,60,126,85,90,59,76,131,88,121,64]
#计算平均心率
average_heart_rate = np.mean(heart_rates)
print(f"The average heart rate is {average_heart_rate:.2f} bpm.")
# 静息心率可以分为三类，如上表所示。确定列表中的心率测量值中有多少落入每类之中，并识别出包含患者数量最多的类别。
resting_heart_rate_categories = {"low": 0, "Normal": 0, "high": 0}
for hr in heart_rates: 
    if hr < 60: 
        resting_heart_rate_categories["low"] += 1
    elif 60 <= hr <= 120: 
        resting_heart_rate_categories["Normal"] += 1
    else: 
        resting_heart_rate_categories["high"] += 1

# 打印每类心率的患者数量
for category, count in resting_heart_rate_categories.items():
    print(f"{category}: {count} patients")

# 接下来，创建一个饼图，该饼图基于初始输入，并报告每个心率类别中的患者数量。
plt.figure(figsize=(8, 8))
plt.pie(resting_heart_rate_categories.values(), labels=resting_heart_rate_categories.keys(), autopct='%1.1f%%')
plt.title('Resting Heart Rate Categories')
plt.show()

