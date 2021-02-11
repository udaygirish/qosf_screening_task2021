import cirq
import numpy as np
import math
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize
import json

# Import Py files
from network_cp import Graph, Edge,create_andsave_graph

import circuit_create as cc 


## Defininig Optimisation method

with open('network.json','r') as f:
    json_data = json.load(f)

Edges = eval(json_data['Edges'])
Weights = eval(json_data['Weights'])
num = json_data['num']
depth = json_data['depth']
rep = json_data['rep']
output_path = json_data['output_path']
max_iter = json_data['max_iter']

if len(list(set(Weights))) == 1:
    print("It is a Unweighted Graph")
    title_graph = 'Unweighted'
else:
    print("It is a weighted Graph")
    title_graph = 'Weighted'

Edges_list = []
for i in Edges:
    Edges_list.append(Edge(i[0],i[1]))


create_andsave_graph(Edges_list,Weights,num,output_path,title_graph)

# Calling the circuit_create Object

# Needed variables num,depth,rep,set_edges,set_weights
cce = cc.circuit_create(num, depth, rep, Edges_list, Weights)

init = [float(random.randint(-314, 314))/float(100) for i in range(0, 2*len(Weights))]

out = minimize(cce.cost_function,x0=init, method='COBYLA', options={'maxiter':max_iter})

optimal_params = out['x']
f = cce.create_circuit(optimal_params)

nums = []
freq = []

for i in range(0, len(f)):
    number = 0
    for j in range(0, len(f[i])):
        number += 2**(len(f[i])-j-1)*f[i][j]
    if (number in nums):
        freq[nums.index(number)] = freq[nums.index(number)] + 1
    else:
        nums.append(number)
        freq.append(1)

freq = [s/sum(freq) for s in freq]

# print(nums)
# print(freq)

x = range(0,2**num)
y = []
for i in range(0,len(x)):
    if(i in nums):
        y.append(freq[nums.index(i)])
    else:
        y.append(0)

plt.bar(x,y)
plt.title(title_graph+"_Probability_Plot")
plt.savefig(output_path+title_graph+"_Probability_Plot.png")
plt.clf()