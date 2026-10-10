import utils

def main():

    nodes,edges,terminals,adj_list = utils.get_toy_graph()

    ## This line visualizes the graph, colors the terminals, and doesn't color any edges. 
    utils.viz_graph(nodes,edges,terminals,[],'orig-graph.html')

    ## 1. Compute Shortest Paths
    #D,pred = shortest_paths(nodes,adj_list,'a')
    #path = utils.get_path('a','j',pred)
    #print(path)


    ## 2. Compute Metric Closure of Graph
    #predecessors, closure_edges = metric_closure(nodes,terminals,adj_list)


    ## 3. Compute Min Spanning Tree (MST) on Metric Closure
    #tree = spanning(closure_edges)


    ## 4. Expand MST Edges
    #final_edges = expand_MST(tree,predecessors)
    #utils.viz_graph(nodes,edges,terminals,final_edges,'steiner-graph.html')

    return

'''
Fill in this function for Part 1.
:param: node_list - list or set of nodes
:param: adj_list - dictionary of (node,set of neighbors) key-value pairs
:param: s - node to begin shortest paths from.
:return: D - dictionary of distances
:return: pred - dictionary of predecessors
'''
def shortest_paths(node_list,adj_list,s):
    print('shortest paths inputs:',node_list,adj_list,s)


    return


'''
Fill in this function for Part 2.
:param: nodes - list or set of nodes in the graph
:param: terminals - list of terminal nodes (nodes for metric closure graph)
:param: adj_list - dictionary of (node, set of neighbors) key-value pairs
:return: predecessors - dictionary of (terminal, pred dictionary) key-value pairs
:return: closure_edges - list of [u,v,weight] edges for the metric closure
'''
def metric_closure(nodes,terminals,adj_list):
    print('metric closure inputs:',nodes,terminals,adj_list)


    return


'''
Fill in this function for Part 3.
:param: edges - list of 3-element edge lists with [u,v,weight].
:return: tree - spanning tree (list of 3-element edge lists)
'''
def spanning(edges):
    print('spanning inputs:',edges)


    return

'''
Fill in this function for Part 4.
:param: tree - minimum spanning tree edges (list of 3-element edge lists)
:param: predecessors - predecessors dictionary from metric_closure()
:return: final_edges - edge list from the original graph that are included in the Steiner tree.
'''

def expand_MST(tree,predecessors):
    print('expand MST inputs:',tree,predecessors)


    return

# Leave this at the bottom of your file.
if __name__ == '__main__':
    main()
