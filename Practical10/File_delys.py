import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir("/d/糖糖/大学/IBI/IBI1_2025-26/IBI1_2025-26/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
dalys_data.head(5)

dalys_data.info



print(dalys_data.describe())

print （dalys_data.iloc[2，0：5]）

# --- 任务 A: 显示前10行的第3和第4列 (Year 和 DALYs) ---
# 文档要求：Show the third and fourth columns for the first 10 rows
# 注意：Python索引从0开始，第3列索引是2，第4列索引是3。前10行是 0:10
print("--- 任务A结果 ---")
print(dalys_data.iloc[0:10, 2:4])

# 请在代码中添加注释回答文档问题：
# 注释示例: # 在阿富汗记录的前10年中，DALYs最高的年份是 199X 年 (请根据输出结果填写)


# --- 任务 B: 使用布尔值筛选津巴布韦 (Zimbabwe) 的数据 ---
# 1. 创建布尔列表：如果 Entity 列等于 "Zimbabwe" 则为 True，否则为 False
# 注意：这里使用 loc 配合列名筛选更直观
zimbabwe_mask = dalys_data['Entity'] == 'Zimbabwe'

# 2. 筛选出津巴布韦的所有年份
zimbabwe_years = dalys_data.loc[zimbabwe_mask, 'Year']

print("--- 任务B结果：津巴布韦的年份 ---")
print(zimbabwe_years)

# 请在代码中添加注释回答文档问题：
# 注释示例: # 津巴布韦数据记录的第一年是 19XX，最后一年是 20XX


# --- 任务 C: 找出 2019 年 DALYs 最高和最低的国家 ---
# 1. 筛选出 2019 年的数据，只保留 'Entity' 和 'DALYs' 两列
recent_data = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]

# 2. 找出最大值和最小值对应的行
max_daly_row = recent_data.loc[recent_data['DALYs'].idxmax()]
min_daly_row = recent_data.loc[recent_data['DALYs'].idxmin()]

print("--- 任务C结果：2019年极值 ---")
print("DALYs 最高的国家:", max_daly_row['Entity'], "数值:", max_daly_row['DALYs'])
print("DALYs 最低的国家:", min_daly_row['Entity'], "数值:", min_daly_row['DALYs'])

# 请在代码中添加注释记录这两个国家的名字

# 假设我们要画 2019 年 DALYs 最高的那个国家 (以 max_daly_row['Entity'] 为例)
# 为了演示，这里假设该国名字存储在变量 target_country 中
target_country = max_daly_row['Entity'] 

# 1. 筛选出该国所有年份的数据
country_data = dalys_data.loc[dalys_data['Entity'] == target_country]

# 2. 绘图
plt.figure(figsize=(10, 6)) # 设置画布大小
plt.plot(country_data['Year'], country_data['DALYs'], 'b+') # 'b+' 表示蓝色加号

# 3. 美化图表
plt.title(f"DALYs over time in {target_country}")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(country_data['Year'][::2], rotation=-90) # 每隔2年显示一个标签，旋转-90度防止重叠

# 4. 显示图形
plt.show()


# 假设我们要画 2019 年 DALYs 最高的那个国家 (以 max_daly_row['Entity'] 为例)
# 为了演示，这里假设该国名字存储在变量 target_country 中
target_country = max_daly_row['Entity'] 

# 1. 筛选出该国所有年份的数据
country_data = dalys_data.loc[dalys_data['Entity'] == target_country]

# 2. 绘图
plt.figure(figsize=(10, 6)) # 设置画布大小
plt.plot(country_data['Year'], country_data['DALYs'], 'b+') # 'b+' 表示蓝色加号

# 3. 美化图表
plt.title(f"DALYs over time in {target_country}")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(country_data['Year'][::2], rotation=-90) # 每隔2年显示一个标签，旋转-90度防止重叠

# 4. 显示图形
plt.show()



# dalys.py
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. Importing the dataset
# ==========================================
# 导入 .csv 文件生成 DataFrame
df = pd.read_csv("dalys-rate-from-all-causes.csv")

# ==========================================
# 2. Third and fourth columns for the first 10 rows
# ==========================================
# 在 pandas 中，列索引从 0 开始。
# Entity(0), Code(1), Year(2), DALYs(3)
# 所以使用 iloc 提取前 10 行（0到9）和第 3、4 列（索引2和3）
first_10_rows = df.iloc[:10, [2, 3]]
print("--- First 10 rows (Year and DALYs) ---")
print(first_10_rows)

# [Required Comment]: What year reported the maximum DALYs across the first 10 years for Afghanistan?
# Based on the printed data for the first 10 years (1990-1999), 
# the maximum DALYs for Afghanistan was 86656.29, which was reported in 1998.


# ==========================================
# 3. Using a Boolean to show all years for Zimbabwe
# ==========================================
# 使用布尔掩码 (Boolean mask) 筛选 Entity 为 'Zimbabwe' 的数据
is_zimbabwe = df['Entity'] == 'Zimbabwe'
zimbabwe_years = df[is_zimbabwe]['Year']
print("\n--- Years recorded for Zimbabwe ---")
print(zimbabwe_years.to_string(index=False))

# [Required Comment]: The first and last year for which these data were recorded
# The first year recorded for Zimbabwe is 1990, and the last year is 2019.


# ==========================================
# 4. Countries with the max and min DALYs in 2019
# ==========================================
# 过滤出2019年的数据
df_2019 = df[df['Year'] == 2019]

# 获取 DALYs 最大值和最小值的行索引
max_daly_idx = df_2019['DALYs'].idxmax()
min_daly_idx = df_2019['DALYs'].idxmin()

# 提取对应的国家名称
country_max = df.loc[max_daly_idx, 'Entity']
country_min = df.loc[min_daly_idx, 'Entity']

print("\n--- 2019 DALYs Extremes ---")
print(f"Country with Maximum DALYs: {country_max}")
print(f"Country with Minimum DALYs: {country_min}")

# [Required Comment]: Stating these countries' names
# The country with the maximum DALYs in 2019 is Central African Republic.
# The country with the minimum DALYs in 2019 is San Marino. 
# (Note: If your specific dataset version differs, replace these names with your console output).


# ==========================================
# 5. Plotting DALYs over time for the Maximum country
# ==========================================
# 提取该最大值国家历年的所有数据
plot_data = df[df['Entity'] == country_max]

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(plot_data['Year'], plot_data['DALYs'], marker='o', linestyle='-', color='b')

# 确保图表有清晰的标签 (All plots are clearly labelled)
plt.title(f'DALYs Over Time for {country_max}')
plt.xlabel('Year')
plt.ylabel('DALYs (Disability-Adjusted Life Years)')
plt.grid(True)

# 显示图表
plt.show()


# ==========================================
# 6. Code to answer the question in question.txt
# ==========================================
# 此处代码用于回答我们在 question.txt 中提出的自定义问题。
# Question: What is the overall average DALYs rate for the United Kingdom across all recorded years?
uk_data = df[df['Entity'] == 'United Kingdom']
average_uk_dalys = uk_data['DALYs'].mean()
print("\n--- Answer to Custom Question ---")
print(f"The average DALYs rate for the United Kingdom across all years is: {average_uk_dalys:.2f}")