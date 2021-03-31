import pytest

import networkx as nx


g = nx.Graph()
g.add_edge('A','B')

g.add_edge('A','C')

g.add_edge('D','B')
g.add_edge('E','B')
g.add_edge('C','F')
g.add_edge('C','G')
l = list(nx.bfs_edges(g, source='A'))

print(l)

