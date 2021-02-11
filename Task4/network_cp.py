''' 
Network Plotter and Creator 
'''

# Import Libraries
import networkx as nx 
import matplotlib.pyplot as plt


# Graph Base Class
class Graph:
    def __init__(self,edges_set):
        self.edges_set = edges_set
        self.node_set = []
        for i in edges_set:
            if (i.start_node not in self.node_set):
                self.node_set.append(i.start_node)
            if (i.end_node not in self.node_set):
                self.node_set.append(i.end_node)
        

# Edge Base Class
class Edge:
    def __init__(self,start_node,end_node):
        self.start_node = start_node
        self.end_node = end_node

def create_andsave_graph(set_edges,set_weights,no_of_nodes,output_path,title_graph):
    G = nx.Graph()
    node_list = [str(i) for i in range(no_of_nodes)]
    for node in node_list:
        G.add_node(node)
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G,pos,node_color='green')

    labels = {}
    for node_name in node_list:
        labels[str(node_name)] =str(node_name)
    nx.draw_networkx_labels(G,pos,labels,font_size=16)

    for i in range(0,len(set_edges)):
        te = set_edges[i]  # Temporary Edge
        tw = set_weights[i] # Temporary Weight
        G.add_edge(str(te.start_node), str(te.end_node), weight = tw)
    unique_weights = list(set(set_weights))

    # Giving a distinct edge look for unique_weights
    for weight in unique_weights:
        weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G.edges(data=True) if edge_attr['weight']==weight]
        width = weight*no_of_nodes*3.0/sum(set_weights)
        nx.draw_networkx_edges(G,pos, edgelist = weighted_edges, width = width)
    
    plt.axis('off')
    plt.title(title_graph+"_Graph_Network")
    plt.savefig(output_path+title_graph+"_Graph_Network.png")
    plt.clf()