import pandas as pd
import graph_structure as gs

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def load_data_as_array(filepath):
    return load_data(filepath).values

def preprocess_data(data):
    #create initial graph
    graph = gs.Graph()

    for sub in data:
        # get element from array that is not nan
        sub_not_nan = []
        for item in sub:
            if type(item) is str:
                sub_not_nan.append(item)
            else:
                break
        
        #add nodes to graph
        for code in sub_not_nan:
            graph.add_node(code)
        
        #add edges to graph
        for i in range(len(sub_not_nan)):
            for j in range(i+1, len(sub_not_nan)):
                graph.add_edge(sub_not_nan[i], sub_not_nan[j])
        
    #normalize edge weight
    graph.normalize_edge_weight()
    
    return graph

if __name__=="__main__":
    FILEPATH = 'dummy.csv'
    data = load_data_as_array(FILEPATH)
    graph = preprocess_data(data)