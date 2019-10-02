import random 
from statistics import mean
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def simulate_timesteps():
    beta = 0.05
    gamma = 0.20
    N = 1000
    N_s = list()
    N_i = list()
    rand_prob = 0
    counter = 0

    while counter < N: 

        time_s = 0
        time_i = 0

        rand_prob = random.random()

        while beta < rand_prob:
            time_s += 1
            rand_prob = random.random()
        
        rand_prob = random.random()

        while(gamma < rand_prob):
            time_i += 1
            rand_prob = random.random()

        N_s.append(time_s)
        N_i.append(time_i)

        counter += 1

    average_time_s = mean(N_s)
    average_time_i = mean(N_i)

    #print(len(N_s) + len(N_i))
    print(N_s[0:10])
    print(N_i[10:20])

    print("Average time in S: {}").format(average_time_s)
    print(average_time_s)
    print("Average time in I: {}").format(average_time_i)
    print(average_time_i)


def simulate_temporal_evolution():
    #Inner function used in calculation
    def beta_prob(infected, total):
        return (0.5 * infected / total)

    gamma = 0.20
    S = 950
    I = 50
    R = 0
    total = 1000
    n = 200
    #dummy_n = 10
    
    matrix = [[S], [I], [R]]


    # Local variables used for this while-loop
    counter = 1
    Y = [S, I, R]
    while counter < n:

        new_infected = sum(np.random.binomial(1, beta_prob(Y[1], total), Y[0]))
        #print(new_infected)
        new_recovered = sum(np.random.binomial(1, gamma, Y[1]))
        #print(new_recovered)

        Y[0] = matrix[0][counter-1]-new_infected
        Y[1] = matrix[1][counter-1]+new_infected-new_recovered
        Y[2] = matrix[2][counter-1]+new_recovered

        #print(Y)

        matrix[0].append(Y[0])
        matrix[1].append(Y[1])
        matrix[2].append(Y[2])

        counter += 1
    
    S_evolution = matrix[0]
    I_evolution = matrix[1]
    R_evolution = matrix[2]
    
    print(S_evolution)
    print(I_evolution, R_evolution)

    x_axis = list(range(0,n))

    plt.plot(x_axis, S_evolution, label = "S_evolution")
    plt.plot(x_axis, I_evolution, label = "I_evolution")
    plt.plot(x_axis, R_evolution, label = "R_evolution")

    # naming the x axis 
    plt.xlabel("Timesteps - n") 
    # naming the y axis 
    plt.ylabel("Population - total") 

    plt.yticks(list(range(0, 951, 50)))

    plt.xticks(list(range(0, 201, 10)))
    
    # giving a title to my graph 
    plt.title("Temporal Evolution - One Realization") 

    plt.legend()
    
    # function to show the plot 
    plt.show() 

        


    
if __name__=="__main__":
    simulate_temporal_evolution()