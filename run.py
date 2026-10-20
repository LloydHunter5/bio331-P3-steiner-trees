import utils

INF = float('inf')

def main():

    nodes,edges,terminals,adj_list = utils.get_toy_graph()

    ## This line visualizes the graph, colors the terminals, and doesn't color any edges. 
    utils.viz_graph(nodes,edges,terminals,[],'orig-graph.html')

    ## 1. Compute Shortest Paths
    D,pred = shortest_paths(nodes,adj_list,'a')
    path = utils.get_path('a','j',pred)
    print(path)


    ## 2. Compute Metric Closure of Graph
    predecessors, closure_edges = metric_closure(nodes,terminals,adj_list)


    ## 3. Compute Min Spanning Tree (MST) on Metric Closure
    tree = spanning(closure_edges)


    ## 4. Expand MST Edges
    final_edges = expand_MST(tree, predecessors)
    utils.viz_graph(nodes,edges,terminals,final_edges,'steiner-graph.html')

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

    # Get the graph. This line prints the graph to the screen.

    # Initialize dicitonary D with all infinity
    D = {}
    pred = {}
    for node in node_list:
        D[node] = INF
        pred[node] = None
    
    D[s] = 0 # distance to start is 0
    Q = [s] # init queue with only s in it

    while len(Q) > 0:
        x = Q.pop(0)
        for neighbor in adj_list[x]:
            if D[neighbor] == INF: # if we haven't visited the node already, update the path length
                D[neighbor] = D[x] + 1
                pred[neighbor] = x
                Q.append(neighbor)
    return D, pred



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

    predecessors = {}
    closure_edges = []
    for u in terminals:
        D, pred = shortest_paths(nodes, adj_list, u)
        # can just give the pred array as is
        predecessors[u] = pred
        for v in terminals:
            # no self loops, and if we already added the edge, we added it in the other order
            if u != v and [v,u, D[v]] not in closure_edges: 
                closure_edges.append([u,v, D[v]])
    return predecessors, closure_edges


def check_create_cycle(edges,u,v):
    """
    Uses a BFS-like traversal to check if there would be a cycle
    if you connect u to v a graph. If u is not in the tree
    or v is not in the tree, then there is no cycle.

    :param: edges (edge list of [node1,node2,weight] elements)
    :param: u (node - string)
    :param: v (node - string)
    :returns: True if there is a cycle and False otherwise
    """

    # generate an (unweighted) adjacency list from the (weighted) edges
    adj_list = utils.edgelist_to_adjlist(edges)
    nodes = utils.get_nodes(edges)

    if u not in adj_list.keys() or v not in adj_list.keys():
        return False
    
    # Then, use BFS-like traversal to check if v is reachable 
    # if you start at u. Begin by copying shortest paths from Lab2 and 
    # modify the code to return True if you reach v when starting at u.
  
    # Initialize dicitonary D with all infinity
    D = {}
    for node in nodes:
        D[node] = INF
    
    D[u] = 0 # distance to start is 0
    Q = [u] # init queue with only u in it

    while len(Q) > 0:
        x = Q.pop(0)
        if x == v: # checks whether we have traversed from u to v
            return True
        for neighbor in adj_list[x]:
            # the distance update, while not needed here,
            # is important so that we don't start looping through
            # cycles. I've decided to keep it as-is here,
            # though it could be made (slightly) more efficient
            if D[neighbor] == INF:
                D[neighbor] = D[x] + 1
                Q.append(neighbor)

    return False



'''
Fill in this function for Part 3.
:param: edges - list of 3-element edge lists with [u,v,weight].
:return: tree - spanning tree (list of 3-element edge lists)
'''
def spanning(edges):
    print('spanning inputs:',edges)
    tree = [] # initialize the empty tree
    # This loop sorts the edges in ascending order by weights 
    for u,v,weight in sorted(edges,key=lambda x: x[2],reverse=False):
        if not check_create_cycle(tree, u, v):
            tree.append([u,v,weight])
    return tree

'''
Fill in this function for Part 4.
:param: tree - minimum spanning tree edges (list of 3-element edge lists)
:param: predecessors - predecessors dictionary from metric_closure()
:return: final_edges - edge list from the original graph that are included in the Steiner tree.
'''

def expand_MST(tree,predecessors):
    print('expand MST inputs:',tree,predecessors)
    final_edges = []
    for edge in tree:
        # grab u and v, ignore weight
        u = edge[0]
        v = edge[1]
        path = utils.get_path(u, v, predecessors[u])
        # since get_path returns an array of nodes in a path, and we need 2-element lists (edges)
        # convert by stepping through the path array with two adjacent pointers
        for i in range(len(path) - 1):
                final_edges.append([path[i],path[i+1]])
    return final_edges

# Leave this at the bottom of your file.
if __name__ == '__main__':
    main()
