import time
import random
import pickle
import copy
import threading
import P_Brain
import P_Functions
network = []
population_size_start = 20 #100
generations = 5 #5
matchups = 20
starts_each = 6 #6 (starts_each sind anspiele pro seite pro matchup)
true_copies_rate = 1 #0.1
mutated_copies_rate = 0 #0.5
old_networks = 0 #0.5
mutation_probability = 0 #0.05
mutation_size = 0.1
cores = 4
threads_available = int(cores * 2)
population_size = population_size_start - (population_size_start % threads_available)
current_generation = 0
################################
answer = input("Weiterentwickeln oder neu erlernen? [1/2]")
if answer == "1":
    if int(old_networks * population_size) < len(pickle.load(open("save.p", "rb"))[0]):
        for i in range(int(old_networks * population_size)):
            network.append(copy.deepcopy(pickle.load(open("save.p", "rb"))[0][i]))
    else:
        for i in range(len(pickle.load(open("save.p", "rb"))[0])):
            network.append(copy.deepcopy(pickle.load(open("save.p", "rb"))[0][i]))
    while len(network) < population_size:
        brain = P_Brain.Brain(8, 4, 1, 8)
        network.append(brain)
else:
    for i in range(population_size):
        brain = P_Brain.Brain(8, 4, 1, 8)
        network.append(brain)
start = time.time()
########################
while current_generation < generations:
    threads = []
    for i in range(threads_available):
        l = []
        for y in range(int(population_size/threads_available)):
            #l.append(network[i * int(population_size/threads_available) + y])
            l.append(network[y * threads_available + i])
        t = threading.Thread(target = P_Functions.training, args = (l, l, matchups, starts_each))
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()
        #print("joined")
    print(P_Functions.print_fitnesses(network))
    print(current_generation)
    P_Functions.plot(network)
    P_Functions.choose_net(network, population_size, true_copies_rate, mutated_copies_rate, mutation_probability, mutation_size)
    current_generation += 1
    print("Expected remaining learning time: ", round((time.time() - start)*(generations-current_generation)/current_generation/60, 1), " min")
##############
print(network[0].weights)
useless_variable = input("Learning process completet. Press Enter to continue..")
P_Functions.show_result(network)