import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edge(1, 2, weight=6)
G.add_edge(1, 3, weight=8)
G.add_edge(1, 4, weight=6)
G.add_edge(2, 4, weight=5)
G.add_edge(2, 5, weight=10)
G.add_edge(3, 4, weight=7)
G.add_edge(3, 5, weight=5)
G.add_edge(3, 6, weight=3)
G.add_edge(5, 6, weight=3)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()})
plt.show()
mst = nx.minimum_spanning_tree(G)
pos = nx.spring_layout(mst)
nx.draw(mst, pos, with_labels=True)
nx.draw_networkx_edge_labels(mst, pos, edge_labels={(u, v): mst[u][v]['weight'] for u, v in mst.edges()})
plt.show()
f=0
for u,v in mst.edges():
    f+=mst[u][v]['weight']
    print(u,"-",v,":" ,mst[u][v]['weight'])
print(f)