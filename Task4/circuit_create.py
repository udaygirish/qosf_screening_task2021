import cirq
import numpy as np 
import math


class circuit_create:
    def __init__(self,num,depth,rep,set_edges,set_weights):
        self.circuit_name = 'MAX_CUT_SOLVER'
        self.num  = num
        self.depth = depth
        self.rep = rep
        self.set_edges = set_edges
        self.set_weights = set_weights
        self.qubits = [cirq.GridQubit(0,i) for i in range(0,num)]


    # Initialize the Qubit

    def initialization(self,qubits):
        for i in qubits:
            yield cirq.H.on(i)

    # Cost Unitary

    def cost_unitary(self,gamma):
        for i in self.set_edges:
            yield cirq.ZZPowGate(exponent=-1*gamma/math.pi).on(self.qubits[i.start_node], self.qubits[i.end_node])
        
    # Mixer Unitary

    def mixer_unitary(self,alpha):
        for i in range(0,len(self.qubits)):
            yield cirq.XPowGate(exponent=-1*alpha/math.pi).on(self.qubits[i])

    def gama_alpha_creator(self,params):
        gamma_list = []
        alpha_list = []
        for i in range(0,len(params),2):
            gamma_list.append(params[i])
            alpha_list.append(params[i+1])
        return gamma_list, alpha_list

    #Definintion -Create Circuit

    def create_circuit(self,params):
        
        self.gamma , self.alpha = self.gama_alpha_creator(params)
        circuit = cirq.Circuit()
        circuit.append(self.initialization(self.qubits))
        for i in range(0, self.depth):
            circuit.append(self.cost_unitary(self.gamma[i]))
            circuit.append(self.mixer_unitary(self.alpha[i]))
        circuit.append(cirq.measure(*self.qubits, key='x'))


        simulator = cirq.Simulator()
        results = simulator.run(circuit, repetitions=self.rep)
        results = str(results)[2:].split(", ")
        new_res = []
        for i in range(0, self.rep):
            hold = []
            for j in range(0, self.num):
                hold.append(int(results[j][i]))
            new_res.append(hold)

        return new_res

    # Definition of cost function - Generalised for weighted graph too

    def cost_function(self,params,):
        av = self.create_circuit(params)
        total_cost = 0

        for i in range(0,len(av)):
            for j in range(0,len(self.set_edges)):
                total_cost += 0.5 * self.set_weights[j] *( ( (1-2*av[i][self.set_edges[j].start_node]) * (1-2*av[i][self.set_edges[j].end_node])) - 1)

        total_cost = float(total_cost)/self.rep

        print("Cost:"+str(total_cost))

        return total_cost

    
    
