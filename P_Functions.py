import copy
import random
import matplotlib.pyplot as plt
import P_Brain
import P_Training
import numpy as np
#old functions: player 1, player 2, ball, sigmoid, print fitnesses
def choose_net(nets, population_size, true_copies_rate, mutated_copies_rate,  mutprob, mutsize):
    #bestes netzwerk vorne
    nets.sort(key = lambda x: x.fitness)
    nets.reverse()
    n = []
    for i in range(int(population_size * true_copies_rate)):
        n.append(copy.deepcopy(nets[i]))
    for i in range(int(population_size * mutated_copies_rate)):
#        child = P_Brain.Brain(8, 4, 1, 8, nets[i], nets[i+1])
        child = copy.deepcopy(nets[i])
        child.mutations_add(mutprob, mutsize)
        n.append(child)
    while len(n) < population_size:
        brain = P_Brain.Brain(8, 4, 1, 8)
        n.append(brain)
    for i in range(population_size):
        n[i].reset_fitness()
    del nets[:]
    nets.extend(copy.deepcopy(n))
def training(nets_left, nets_right, matchups, starts_each):
    for i in range(matchups):
        random_left = []
        for j in range(len(nets_left)):
            random_left.append(j)
        random_right = []
        for j in range(len(nets_right)):
            random_right.append(j)
        for y in range(len(nets_left)):
            choice_left = random.choice(random_left)
            random_left.remove(choice_left)
            choice_right = random.choice(random_right)
            random_right.remove(choice_right)
            t = P_Training.Training()
            t.play(nets_left[choice_left], nets_right[choice_right], starts_each)
def plot(list):
    m, b = np.polyfit(range(len(list)), print_fitnesses(list), 1)
    plt.close()
    for i in range(len(list)):
        plt.scatter(i, print_fitnesses(list)[i] , c = get_colors(list)[i])
    plt.plot([0, len(list)], [b, m * len(list) + b])
    plt.show(block = False)
def print_fitnesses(n):
    l = []
    for i in n:
        l.append(round(i.fitness, 2))
    return l
def get_colors(n):
    l = []
    for i in range(len(n)):
        l.append(tuple(copy.deepcopy(n[i].color)))
    return l
def show_result(nets):
    t = P_Training.Training()
    t.show(nets)