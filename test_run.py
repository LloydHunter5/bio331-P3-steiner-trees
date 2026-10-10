import run
import utils

nodes,edges,terminals,adj_list = utils.get_toy_graph()

def test_shortest_paths_distances():
    D,pred = run.shortest_paths(nodes,adj_list,'a')
    test_D = {'a': 0, 'b': 1, 'c': 1, 'd': 2, 'e': 2, 'f': 3, 'g': 2, 'h': 2, 'i': 3, 'j': 4, 'k': 3, 'l': 4, 'm': 5}
    for key in test_D:
        assert key in D
        assert D[key] == test_D[key]
    return

def test_shortest_paths_preds():
    D,pred = run.shortest_paths(nodes,adj_list,'a')
    test_pred = {'a': None, 'b': 'a', 'c': 'a', 'd': 'b', 'e': 'c', 'f': 'g', 'g': 'c', 'h': 'c', 'i': 'h', 'j': 'i', 'k': 'h', 'l': 'i', 'm': 'l'}
    for key in ['a','b','d','c','h','i','l','m','f']: # only check preds that aren't ambiguous
        assert key in test_pred
        assert pred[key] == test_pred[key]
    return

def test_closure_edges():
    predecessors, closure_edges = run.metric_closure(nodes,terminals,adj_list)
    test_closure_edges =  [['b', 'd', 1], ['b', 'i', 3], ['b', 'k', 3], ['d', 'i', 4], ['d', 'k', 3], ['i', 'k', 2]]
    assert len(closure_edges) == len(test_closure_edges)
    for u,v,w in closure_edges:
        assert [u,v,w] in test_closure_edges or [v,u,w] in test_closure_edges
    return

def test_predecessors():
    predecessors, closure_edges = run.metric_closure(nodes,terminals,adj_list)
    assert len(predecessors) == len(terminals)
    b_pred = predecessors['b']
    test_b_pred = {'a': 'b', 'b': None, 'c': 'b', 'd': 'b', 'e': 'b', 'f': 'g', 'g': 'c', 'h': 'c', 'i': 'h', 'j': 'i', 'k': 'h', 'l': 'i', 'm': 'l'}
    assert len(b_pred) == len(test_b_pred)
    for key in ['b','a','c','d','e','h','m','i','f']: # only check predecessors that aren't ambiguous
        assert key in test_b_pred
        assert b_pred[key] == test_b_pred[key]
    return

def test_mst():
    predecessors, closure_edges = run.metric_closure(nodes,terminals,adj_list)
    tree = run.spanning(closure_edges)
    assert len(tree) == 3 # check that there are three edges
    assert tree[0][2]+tree[1][2]+tree[2][2] == 6 # check that the costs sum to 6
    for u,v,w in tree: # check that all the nodes are terminals
        assert u in terminals
        assert v in terminals
    return
