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