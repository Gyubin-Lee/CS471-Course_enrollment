#define features for nodes
class Feature:
    def __init__(self, major, level):
        self.major = major
        self.level = level

#define node class for graph
class Node:
    def __init__(self, code):
        self.code = code
        self.feature = None
        self.edges = []
    
    def set_feature_from_code(self, code):
        # if code is 'CS320', major is 'CS' and level is 3
        major = code[:-3]
        level = int(code[-3:][0])
        self.feature = Feature(major, level)

#define undirected edge class for graph
class Edge:
    def __init__(self, node1, node2):
        INIT_WEIGHT = 1

        self.weight = INIT_WEIGHT
        self.nodes_pair = set([node1, node2])
    
    def increase_weight(self):
        self.weight += 1

#define graph class
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def get_all_codes(self):
        codes = []
        for node in self.nodes:
            codes.append(node.code)
        return codes

    def get_all_nodes_pair(self):
        nodes_pair = []
        for edge in self.edges:
            nodes_pair.append(edge.nodes_pair)
        return nodes_pair

    def find_nodes_pair_index(self, node1, node2):
        for i, edge in enumerate(self.edges):
            if (node1 in edge.nodes_pair) and (node2 in edge.nodes_pair):
                return i
        return None

    def normalize_edge_weight(self):
        #get maximum weight
        max_weight = max([edge.weight for edge in self.edges])
        #normalize weight
        for edge in self.edges:
            edge.weight = edge.weight / max_weight
    
    def add_node(self, code):
        #check if node already exists
        if (code in self.get_all_codes()):
            return
        
        new_node = Node(code)
        new_node.set_feature_from_code(code)       
        self.nodes.append(new_node)
    
    def add_edge(self, node1, node2):
        #check if edge already exists
        if (set([node1, node2]) in self.get_all_nodes_pair()):
            i = self.find_nodes_pair_index(node1, node2)
            self.edges[i].increase_weight()
            return
        
        edge = Edge(node1, node2)
        self.edges.append(edge)