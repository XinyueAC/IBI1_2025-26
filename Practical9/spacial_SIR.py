# --- 4. 时间循环 ---
for t in range(T):
    # --- 4.1 找出所有感染者的坐标 ---
    # np.where 返回满足条件的坐标
    infected_points = np.where(population == 1)
    # zip 将 x坐标 和 y坐标 配对
    infected_list = list(zip(infected_points[0], infected_points[1]))
    
    # --- 4.2 遍历每一个感染者 ---
    for x, y in infected_list:
        # --- 4.2.1 尝试康复 ---
        # 每个感染者有 gamma 的概率康复
        if np.random.rand() < gamma:
            population[x, y] = 2 # 变为康复状态
            continue # 如果已经康复，就不再传播疾病
        
        # --- 4.2.2 尝试感染邻居 (8个方向) ---
        # 遍历周围8个格子
        for x_offset in [-1, 0, 1]:
            for y_offset in [-1, 0, 1]:
                # 跳过自己 (0, 0)
                if x_offset == 0 and y_offset == 0:
                    continue
                
                # 计算邻居坐标
                x_neigh = x + x_offset
                y_neigh = y + y_offset
                
                # --- 4.2.3 边界检查 ---
                # 确保邻居在地图范围内
                if 0 <= x_neigh < grid_size and 0 <= y_neigh < grid_size:
                    # --- 4.2.4 感染检查 ---
                    # 只有当邻居是易感者(0)时才可能被感染
                    if population[x_neigh, y_neigh] == 0:
                        # 掷骰子决定是否感染
                        if np.random.rand() < beta:
                            population[x_neigh, y_neigh] = 1 # 变为感染状态
    
    # --- 4.3 绘图 (每10步画一次，或者只画特定的步数) ---
    # 为了不产生太多窗口，我们可以只在特定时间点画图
    if t in [0, 10, 50, 99]:
        plt.figure(figsize=(6,4), dpi=150)
        # 使用 viridis 颜色映射
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time = {t}')
        plt.savefig(f'Spatial_SIR_t{t}.png')
        plt.show()


import numpy as np
import matplotlib.pyplot as plt

size = 100
beta = 0.3
gamma = 0.05
T = 100

# 0=易感, 1=感染, 2=康复
grid = np.zeros((size, size), dtype=int)

# 随机1个初始感染
x, y = np.random.choice(size, 2)
grid[x, y] = 1

# 8邻域
neighbors = [(-1,-1), (-1,0), (-1,1),
             (0,-1),          (0,1),
             (1,-1),  (1,0), (1,1)]

for step in range(T):
    new_grid = grid.copy()
    inf_pos = np.where(grid == 1)
    
    for i, j in zip(inf_pos[0], inf_pos[1]):
        # 康复
        if np.random.rand() < gamma:
            new_grid[i, j] = 2
        
        # 感染邻居
        for di, dj in neighbors:
            ni = i + di
            nj = j + dj
            if 0 <= ni < size and 0 <= nj < size:
                if grid[ni, nj] == 0 and np.random.rand() < beta:
                    new_grid[ni, nj] = 1
    
    grid = new_grid

    # 每步画图
    plt.clf()
    plt.imshow(grid, cmap='viridis', interpolation='nearest')
    plt.title(f'Time = {step}')
    plt.pause(0.1)

plt.show()