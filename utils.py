from pyvis.network import Network
import sys

'''
Get example undirected, unweighted graph.
'''
def get_toy_graph():
    edges = read_edges('files/toy-edges.txt')
    nodes = set()
    for u,v in edges:
        nodes.add(u)
        nodes.add(v)
    terminals = open('files/toy-terminals.txt').readline().strip().split()
    adj_list = edgelist_to_adjlist(edges)

    print('%d nodes, %d terminals, and %d edges' % (len(nodes),len(terminals),len(edges)))
    return nodes,edges,terminals,adj_list

'''
Reads unweighted, undirected edges from a two-column file.
:param: fname - string - filename
:return: list of two-element lists
'''
def read_edges(fname):
    edges = []
    with open(fname) as fin:
        for line in fin:
            row = line.strip().split()
            edges.append([row[0],row[1]])
    return edges

'''
Convert an edge list to an adjacency list.
'''
def edgelist_to_adjlist(edgelist):
    L = {} # initialize adjacency list
    for edge in edgelist:
        if len(edge) == 2:
            u,v = edge
        else:
            u,v,ignore = edge 
        if u not in L: # add u to L if not already there
            L[u] = set()
        if v not in L: # add v to L if not already there
            L[v] = set()
        # add neighbor v to L[u] and u to L[v] (undirected)
        L[u].add(v)
        L[v].add(u)
    return L

'''
# Visualizes a graph with a Steiner tree.
# input: nodes - list of nodes (strings)
# input: edges -  edge list of [node1,node2] elements
# input: terminals - list of nodes (strings)
# input: tree - edge list [node1,node2] elements for the tree
# input outfile - string that ends in '.html'.
# returns: nothing.
'''
def viz_graph(nodes,edges,terminals,tree,outfile):
    nonterminal_color = '#FFFFFF'
    nonterminal_node_shape = 'circle'

    terminal_color = '#73d3ef'
    terminal_node_shape = 'circle'

    nontree_edge_color = '#AAAAAA'
    tree_edge_color = '#000000'
    
    G = Network(directed=False)
    for n in nodes:
        if n in terminals:
            G.add_node(n,label=str(n),widthConstraint=25,heightConstraint=25,color=terminal_color,shape=terminal_node_shape)
        else:
            G.add_node(n,label=str(n),widthConstraint=25,heightConstraint=25,color=nonterminal_color,shape=nonterminal_node_shape)

    for u,v in edges:
        if [u,v] in tree or [v,u] in tree:
            G.add_edge(u,v,color=tree_edge_color,width=4)
        else:
            G.add_edge(u,v,color=nontree_edge_color,width=1)
    
    G.toggle_physics(True)
    G.write_html(outfile)
    print('Saved file as',outfile)
    return

'''
Given a source node u and a target node v and a dictionary preds of predecessors,
returns the shortest path from u to v.  If there are multiple paths, only
one is returned.  Returned path is a list of nodes.
'''
def get_path(u,v,preds,verbose=False):
    current = v # start at the END of the path.
    if preds[current] == None:
        sys.exit(f'ERROR! Node {v} has no predecessor in preds variable.')
    path = [] # empty path
    if verbose:
        print('starting:',path,'with current',current)
    while current != None: # if we're not at the START of the path...
        path = [current] + path ## add element to beginning of path
        current = preds[current] ## update current to be the predecessor.
        if verbose:
            print('-->',path,'new current',current)
    if verbose:
        print('returning:',path)
    return path


'''
Takes a weighted edgelist and gets a node set from it.
Copied from L4.
'''
def get_nodes(edgelist):
    nodes = set()
    for u,v,ignore in edgelist:
        nodes.add(u)
        nodes.add(v)
    return list(nodes)
