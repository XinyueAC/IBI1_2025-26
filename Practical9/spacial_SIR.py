


import numpy as np
import matplotlib.pyplot as plt

size = 100
beta = 0.3
gamma = 0.05
T = 100

# 0=易感, 1=感染, 2=康复
grid = np.zeros((size, size), dtype=int)

x, y = np.random.choice(size, 2)
grid[x, y] = 1


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
        
      
        for di, dj in neighbors:
            ni = i + di
            nj = j + dj
            if 0 <= ni < size and 0 <= nj < size:
                if grid[ni, nj] == 0 and np.random.rand() < beta:
                    new_grid[ni, nj] = 1
    
    grid = new_grid


    plt.clf()
    plt.imshow(grid, cmap='viridis', interpolation='nearest')
    plt.title(f'Time = {step}')
    plt.pause(0.1)

plt.show()