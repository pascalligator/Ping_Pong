import random
import math
import copy
def sigmoid(x):
  return 1 / (1 + math.exp(-x))
class Brain():
    def __init__(self, inputs = None, outputs = None, layers = None, neurons = None, net1 = None, net2 = None):
        if net1 == None:
            # weights #
            l=[]
            l.append([])
            for i in range(inputs):
                l[0].append([])
                for i in range(neurons):
                    l[0][-1].append(random.uniform(-1, 1))
            for p in range(layers - 1):
                l.append([])
                for i in range(neurons):
                    l[-1].append([])
                    for i in range(neurons):
                        l[-1][-1].append(random.uniform(-1, 1))
            l.append([])
            for i in range(neurons):
                l[-1].append([])
                for y in range(outputs):
                    l[-1][-1].append(random.uniform(-1, 1))
            self.inputs = inputs
            self.outputs = outputs
            self.weights = copy.deepcopy(l)
            self.layers = layers
            self.neurons = neurons
            self.fitness = 0
            self.color = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
            # bias #
            b = []
            for i in range(layers):
                b.append([])
                for y in range(neurons):
                    b[-1].append(random.uniform(-1, 1))
            b.append([])
            for i in range(outputs):
                b[-1].append(random.uniform(-1, 1))
            self.bias = copy.deepcopy(b)
        else:
            # weights #
            l=[]
            l.append([])
            for i in range(net1.inputs):
                l[0].append([])
            for i in range(net1.neurons):
                rand = random.randint(0,1)
                for y in range(net1.inputs):
                    if rand == 0:
                        l[0][y].append(net1.weights[0][y][i])
                    else:
                        l[0][y].append(net2.weights[0][y][i])
            for i in range(net1.layers - 1):
                l.append([])
                for y in range(net1.neurons):
                    l[-1].append([])
            for u in range(net1.layers - 1):
                for i in range(net1.neurons):
                    rand = random.randint(0,1)
                    for y in range(net1.neurons):
                        if rand == 0:
                            l[u+1][y].append(net1.weights[u+1][y][i])
                        else:
                            l[u+1][y].append(net2.weights[u+1][y][i])
            l.append([])
            for i in range(net1.neurons):
                l[-1].append([])
            for i in range(net1.outputs):
                rand = random.randint(0,1)
                for y in range(net1.neurons):
                    if rand == 0:
                        l[-1][y].append(net1.weights[-1][y][i])
                    else:
                        l[-1][y].append(net2.weights[-1][y][i])
            self.inputs = inputs
            self.outputs = outputs
            self.weights = copy.deepcopy(l)
            self.layers = net1.layers
            self.neurons = net1.neurons
            self.fitness = net1.fitness
            self.color = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
            # bias #
            b = []
            for i in range(layers):
                b.append([])
                for y in range(neurons):
                    rand = random.randint(0,1)
                    if rand == 0:
                        b[-1].append(net1.bias[i][y])
                    else:
                        b[-1].append(net2.bias[i][y])
            b.append([])
            for i in range(outputs):
                rand = random.randint(0,1)
                if rand == 0:
                    b[-1].append(net1.bias[-1][i])
                else:
                    b[-1].append(net2.bias[-1][i])
            self.bias = copy.deepcopy(b)
    #ask network
    def net(brain, inp):
        all_neurons = []
        for i in range(brain.layers*brain.neurons + brain.inputs + brain.outputs):
            all_neurons.append(0)
        for i in range(brain.inputs):
            all_neurons[i] += inp[i]
        for y in range(brain.inputs):
            for j in range(brain.neurons):
                all_neurons[brain.inputs+j] += all_neurons[y]*brain.weights[0][y][j]
        for i in range(brain.neurons):
            all_neurons[brain.inputs+i] = math.tanh(all_neurons[brain.inputs + i] + brain.bias[0][i])
        for i in range(brain.layers - 1):
            for y in range(brain.neurons):
                for j in range(brain.neurons):
                    all_neurons[brain.inputs+(i+1)*brain.neurons+j] += all_neurons[brain.inputs+i*brain.neurons+y]*brain.weights[1+i][y][j]
            for y in range(brain.neurons):
                all_neurons[brain.inputs+i*brain.neurons+y] = math.tanh(all_neurons[brain.inputs+(i+1)*brain.neurons+y] + brain.bias[i+1][y])
        for y in range(brain.neurons):
            for j in range(brain.outputs):
                all_neurons[brain.inputs+brain.neurons*brain.layers+j] += all_neurons[brain.inputs+brain.neurons*(brain.layers-1)+y]*brain.weights[-1][y][j]
        for i in range(brain.outputs):
            all_neurons[-i-1] = math.tanh(all_neurons[-i-1] + brain.bias[-1][i])
        outputs = []
        for i in range(brain.outputs):
            outputs.append(all_neurons[-i-1])
        return outputs
    def mutations_add(self, mutprob, mutsize):
        if mutprob != 0:
            for y in range(self.inputs):
                for j in range(self.neurons):
                    a = self.weights[0][y][j]
                    seq = []
                    seq.append(-1)
                    for p in range(int(1/mutprob)):
                        seq.append(1)
                    rand = random.choice(seq)
                    if rand == -1:
                        a += random.uniform(-mutsize, mutsize)
                    self.weights[0][y].pop(j)
                    self.weights[0][y].insert(j, a)
            for i in range(self.layers - 2):
                for y in range(self.neurons):
                    for j in range(self.neurons):
                        a = self.weights[i+1][y][j]
                        seq = []
                        seq.append(-1)
                        for p in range(int(1/mutprob)):
                            seq.append(1)
                        rand = random.choice(seq)
                        if rand == -1:
                            a += random.uniform(-mutsize, mutsize)
                        self.weights[i+1][y].pop(j)
                        self.weights[i+1][y].insert(j, a)
            for y in range(self.neurons):
                for j in range(self.outputs):
                    a = self.weights[self.layers][y][j]
                    seq = []
                    seq.append(-1)
                    for p in range(int(1/mutprob)):
                        seq.append(1)
                    rand = random.choice(seq)
                    if rand == -1:
                        a += random.uniform(-mutsize, mutsize)
                    self.weights[self.layers][y].pop(j)
                    self.weights[self.layers][y].insert(j, a)
            # bias #
            for i in range(self.layers):
                for y in range(self.neurons):
                    a = self.bias[i][y]
                    seq = []
                    seq.append(-1)
                    for p in range(int(1/mutprob)):
                        seq.append(1)
                    rand = random.choice(seq)
                    if rand == -1:
                        a += random.uniform(-0.5, 0.5)
                    self.bias[i].pop(y)
                    self.bias[i].insert(y, a)
            for i in range(self.outputs):
                a = self.bias[-1][i]
                seq = []
                seq.append(-1)
                for p in range(int(1/mutprob)):
                    seq.append(1)
                rand = random.choice(seq)
                if rand == -1:
                    a += random.uniform(-0.5, 0.5)
                self.bias[-1].pop(i)
                self.bias[-1].insert(i, a)
    def mutations(self, mutprob):
        for y in range(self.inputs):
            for j in range(self.neurons):
                a = self.weights[0][y][j]
                seq = []
                seq.append(-1)
                for p in range(int(1/mutprob)):
                    seq.append(1)
                a *= random.choice(seq)
                self.weights[0][y].pop(j)
                self.weights[0][y].insert(j, a)
        for i in range(self.layers - 2):
            for y in range(self.neurons):
                for j in range(self.neurons):
                    a = self.weights[i+1][y][j]
                    seq = []
                    seq.append(-1)
                    for p in range(int(1/mutprob)):
                        seq.append(1)
                    a *= random.choice(seq)
                    self.weights[i+1][y].pop(j)
                    self.weights[i+1][y].insert(j, a)
        for y in range(self.neurons):
            for j in range(self.outputs):
                a = self.weights[self.layers][y][j]
                seq = []
                seq.append(-1)
                for p in range(int(1/mutprob)):
                    seq.append(1)
                a *= random.choice(seq)
                self.weights[self.layers][y].pop(j)
                self.weights[self.layers][y].insert(j, a)
        # bias #
        for i in range(self.layers):
            for y in range(self.neurons):
                a = self.bias[i][y]
                seq = []
                seq.append(-1)
                for p in range(int(1/mutprob)):
                    seq.append(1)
                a *= random.choice(seq)
                self.bias[i].pop(y)
                self.bias[i].insert(y, a)
        for i in range(self.outputs):
            a = self.bias[-1][i]
            seq = []
            seq.append(-1)
            for p in range(int(1/mutprob)):
                seq.append(1)
            a *= random.choice(seq)
            self.bias[-1].pop(i)
            self.bias[-1].insert(i, a)
    def reset_fitness(self):
        self.fitness = 0
    def add_layer(self):
        self.weights.insert(self.layers + 1, [])
        for i in range(self.neurons - 2):
            self.weights[self.layers].append([])
            for y in range(self.outputs):
                self.weights[self.layers][-1].append(0)
        for i in range(self.outputs):
            self.weights[self.layers].append([])
            for y in range(self.outputs):
                self.weights[self.layers][-1].append(0)
        self.layers += 1
    def add_neuron(self):
        for i in range(self.inputs):
            self.weights[0][i].append(0)
        for i in range(self.layers - 1):
            self.weights[i+1].append([])
            for y in range(self.neurons + 1):
                self.weights[i+1][-1].append(0)
        self.weights[self.layers].append([])
        for i in range(self.outputs):
            self.weights[self.layers][-1].append(0)            
        self.neurons += 1
