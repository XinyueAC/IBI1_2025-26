import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05
T = 1000

# 测试不同疫苗接种率
vaccine_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.figure(figsize=(6,4), dpi=150)

for i, vac_rate in enumerate(vaccine_rates):
    V = int(N * vac_rate)
    S = max(N - V - 1, 0)
    I = 1
    R = 0
    
    I_list = [I]
    
    for t in range(T):
        infection_prob = beta * (I / N)

        S = max(S, 0)

        new_infected = np.random.binomial(S, infection_prob)
        new_recovered = np.random.binomial(I, gamma)
        
        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered
        
        I_list.append(I)
    
    plt.plot(I_list, label=f'{int(vac_rate*100)}%', color=cm.viridis(i*25))

plt.xlabel('Time')
plt.ylabel('Infected')
plt.title('SIR with Vaccination')
plt.legend()
plt.savefig('SIR_vaccination.png')
plt.show()