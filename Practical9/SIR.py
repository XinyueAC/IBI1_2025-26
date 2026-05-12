
import numpy as np
import matplotlib.pyplot as plt


N = 10000          
beta = 0.3         
gamma = 0.05      
T = 1000           

S_count = 9999     # Susceptible
I_count = 1        # Infected
R_count = 0        # Recovered


S_history = [S_count]
I_history = [I_count]
R_history = [R_count]

# 2. 模拟时间过程
for t in range(T):
    p_infect = beta * (I_count / N)
    
    # Ensure that the probability does not exceed 1 (boundary condition protection)
    p_infect = min(p_infect, 1.0)
    

    new_infections = np.sum(np.random.choice([0, 1], size=S_count, p=[1 - p_infect, p_infect]))

    new_recovered = np.sum(np.random.choice([0, 1], size=I_count, p=[1 - gamma, gamma]))
    
    
    S_count -= new_infections
    I_count += (new_infections - new_recovered)
    R_count += new_recovered
    
    # Record the data at the current time point
    S_history.append(S_count)
    I_history.append(I_count)
    R_history.append(R_count)


plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_history, label='susceptible')
plt.plot(I_history, label='infected')
plt.plot(R_history, label='recovered')

plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()


plt.savefig("SIR_model.png", format="png")
plt.show()