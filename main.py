import random 
from statistics import mean
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Task 1 d)
def simulate_timesteps():
    # Variables given by task
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
        
        # This is the step from state S to state I
        time_s += 1
        
        rand_prob = random.random()

        while gamma < rand_prob:
            time_i += 1
            rand_prob = random.random()
        
        # This is the step from state I to R
        time_i += 1

        N_s.append(time_s)
        N_i.append(time_i)

        counter += 1

    average_time_s = np.mean(N_s)
    average_time_i = np.mean(N_i)

 
    print ("------------------------------")
    print ("Task 1d)")
    print ("Average time in state S: {mean}".format(mean=average_time_s))
    print ("Average time in state I: {mean}".format(mean=average_time_i))


# Task 1 e)
def simulate_temporal_evolution():
    #Inner function used in calculation
    def beta_prob(infected, total):
        return (0.5 * infected / total)

    # Variables given by task
    gamma = 0.20
    S = 950
    I = 50
    R = 0
    total = 1000
    n = 200
    
    matrix = [[S], [I], [R]]


    # Local variables used for this while-loop
    counter = 1
    Y = [S, I, R]
    while counter < n:
        
        new_infected = sum(np.random.binomial(1, beta_prob(Y[1], total), Y[0]))
        new_recovered = sum(np.random.binomial(1, gamma, Y[1]))
       
        Y[0] = matrix[0][counter-1]-new_infected
        Y[1] = matrix[1][counter-1]+new_infected-new_recovered
        Y[2] = matrix[2][counter-1]+new_recovered

        matrix[0].append(Y[0])
        matrix[1].append(Y[1])
        matrix[2].append(Y[2])

        counter += 1

    return matrix

# Task 1 e continued. Plot the simulation to a graph, to show the temporal evolution through time steps
def plot_temporal_evolution(matrix):
    S_evolution = matrix[0]
    I_evolution = matrix[1]
    R_evolution = matrix[2]
    

    x_axis = list(range(0,200))

    plt.plot(x_axis, S_evolution, label = "S_evolution")
    plt.plot(x_axis, I_evolution, label = "I_evolution")
    plt.plot(x_axis, R_evolution, label = "R_evolution")

    # naming the x axis 
    plt.xlabel("Timesteps - n") 
    # naming the y axis 
    plt.ylabel("Population - total") 

    plt.yticks(list(range(0, 951, 50)))

    plt.xticks(list(range(0, 201, 20)))
    
    # giving a title to my graph 
    plt.title("Temporal Evolution - One Realization") 

    plt.legend()
    
    # function to show the plot 
    # plt.show()

    # function to save the figure as png file in current dir
    plt.savefig("task1e_figure", bbox_inches="tight")


# Task 1 f)
def simulate_expected_max_infected():
    n = 1000
    counter = 0
    I_max = []
    I_timesteps = []
    while counter < n:
        matrix = simulate_temporal_evolution()
        I_max.append(max(matrix[1]))
        I_timesteps.append(np.argmax(matrix[1]))
        counter += 1
    
    print ("------------------------------")
    print ("Task 1f)")
    print ("Based on {n} simulations of the outbreak for {timesteps} timesteps, the calculated expected number of max infected is: {mean}\n".format(n=n, timesteps=200, mean=np.mean(I_max)))
    print ("And based on the same simulations, the expected timestep at which the infected individuals first takes its highest value: {argmax_mean}".format(argmax_mean=np.mean(I_timesteps)))
    
   

if __name__=="__main__":
    simulate_timesteps()
    simulate_expected_max_infected()
    matrix = simulate_temporal_evolution()
    plot_temporal_evolution(matrix)