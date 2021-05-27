# Search methods

import search
ab = search.GPSProblem('A', 'B'
                       , search.romania)

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())
node, count = search.sorted_graph_search(ab)
print(node.path())
print(count)
# print(search.sorted_graph_search(ab)[0].path())
node, count = search.H_graph_search(ab)
print(node.path())
print(count)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
