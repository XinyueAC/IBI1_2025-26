import numpy as np
import matplotlib.pyplot as plt 
#def SIR(S0, I0, R0, beta, gamma, days):
#    S = np.zeros(days)
#    I = np.zeros(days)
#    R = np.zeros(days)
#    
#    S[0] = S0
#    I[0] = I0
#    R[0] = R0
#    
#    for t in range(1, days):
#        dS = -beta * S[t-1] * I[t-1] / (S[t-1] + I[t-1] + R[t-1])
#        dI = beta * S[t-1] * I[t-1] / (S[t-1] + I[t-1] + R[t-1]) - gamma * I[t-1]
#        dR = gamma * I[t-1]
#        
#        S[t] = S[t-1] + dS
#        I[t] = I[t-1] + dI
#        R[t] = R[t-1] + dR
#        
#    return S, I, R
Q
#define the basic variables of the model, one for each of the population (Susceptible,Infected, and Recovered)
#Initially, we start with a population of 10 000 people. 
#Initially, one person is infected, the rest of the population is Susceptible (nobody has yet recovered).

I0 = 1
R0 = 1
N = 10000
beta = 0.3
gamma = 0.05
#You will also want to create arrays for each of your variables to track how they evolve over
#time. (Recall that you can define an array using square brackets [] and that you can later
#add elements to an array using the append() function)
days = 160
S = np.zeros(days)
I = np.zeros(days)
R = np.zeros(days)

# --- 2. 创建数组来存储随时间变化的数据 ---
# 我们将模拟1000个时间步
T = 1000
S = [S0] # 易感者数组，初始值为S0
I = [R0] # 感染者数组，初始值为R0
R = [P0] # 康复者数组，初始值为P0

# --- 3. 时间循环 ---
for t in range(T):
    # 获取当前时刻的人数
    s = S[-1]
    i = I[-1]
    
    # --- 计算感染 ---
    # 感染概率 = beta * (感染者比例)
    # 注意：这里文档提示了要乘以感染者比例 i/N
    prob_infect = beta * (i / N)
    
    # 使用二项分布计算新感染人数
    # np.random.binomial(n, p): 从n个样本中，以概率p发生事件的次数
    new_infected = np.random.binomial(s, prob_infect)
    
    # --- 计算康复 ---
    # 康复概率 = gamma
    new_recovered = np.random.binomial(i, gamma)
    
    # --- 更新下一轮的人数 ---
    # 易感者减少(被感染的)，感染者增加(新感染的)减少(康复的)
    s_new = s - new_infected
    i_new = i + new_infected - new_recovered
    r_new = R[-1] + new_recovered # 康复者增加
    
    # 将新数据添加到数组末尾
    S.append(s_new)
    I.append(i_new)

    # --- 4. 绘图 ---
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')

plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('SIR Model')
plt.legend()
plt.savefig('SIR_plot.png') # 保存图片
plt.show()



# SIR.py
# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt

# 1. 定义模型的基本参数
N = 10000          # 总人口
beta = 0.3         # 接触感染率
gamma = 0.05       # 康复率
T = 1000           # 模拟的总时间步长

# 初始人群状态
S_count = 9999     # 易感人数 (Susceptible)
I_count = 1        # 初始感染人数 (Infected)
R_count = 0        # 康复人数 (Recovered)

# 用于记录随时间变化的数据的数组 (列表)
S_history = [S_count]
I_history = [I_count]
R_history = [R_count]

# 2. 模拟时间过程
for t in range(T):
    # 计算当前时间点每个易感者被感染的概率 (需乘以人群中感染者的比例)
    p_infect = beta * (I_count / N)
    
    # 确保概率不超过 1 (边界条件保护)
    p_infect = min(p_infect, 1.0)
    
    # 使用 np.random.choice 模拟人群的随机转移 
    # 对于每个易感者，依据概率 p_infect 决定是否变为感染者 (1为感染，0为未感染)
    new_infections = np.sum(np.random.choice([0, 1], size=S_count, p=[1 - p_infect, p_infect]))
    
    # 对于每个感染者，依据概率 gamma 决定是否康复
    new_recovered = np.sum(np.random.choice([0, 1], size=I_count, p=[1 - gamma, gamma]))
    
    # 更新各人群总数
    S_count -= new_infections
    I_count += (new_infections - new_recovered)
    R_count += new_recovered
    
    # 记录当前时间点的数据
    S_history.append(S_count)
    I_history.append(I_count)
    R_history.append(R_count)

# 3. 绘制并保存结果
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_history, label='susceptible')
plt.plot(I_history, label='infected')
plt.plot(R_history, label='recovered')

plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()

# 保存图像并显示
plt.savefig("SIR_model.png", type="png")
plt.show()