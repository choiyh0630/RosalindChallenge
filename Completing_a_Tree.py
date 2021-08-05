# Taxon = A collection of species clumped together.
# For a given collection of taxa, a phylogeny is a treelike diagram that best represents the evolutionary connections between the taxa.

# A tree is a connected (undirected) graph containing no cycles.
# In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having
# a degree larger than 1 is called an internal node.

# Given: A positive integer n (n <= 1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
# Return: The minimum number of edges that can be added to the graph to produce a tree.

# 1. Identify number of clusters (including independent nodes)
# 2. Min # of edges = number of clusters - 1

from collections import defaultdict

f = open('rosalind_tree.txt', 'r')
l = f.read().splitlines()

total_nodes = int(l[0])
adj_lst = defaultdict(list)
for i in l[1:]:
    v, w = i.split(' ')
    adj_lst[int(v)].append(int(w))
    adj_lst[int(w)].append(int(v))

print(adj_lst)

def dfs(node, visited):
    if node in visited:
        return visited
    if node not in visited:
        visited.append(node)
    for neighbor in adj_lst[node]:
        dfs(neighbor, visited)
    return visited

print(dfs(5, []))

already = []
count = 0
for node in range(1, total_nodes + 1):
    if node not in already:
        count += 1
        already += dfs(node, [])
print(f'number of clusters: {count}')
print(f'minimum number of edges to make a tree: {count - 1}')

# x = []
# def f(x):
#     x.append(1)
#
#     return
# f(x)
# print(x)
#
# def g(x):
#     for i in range(3):
#         x += i
#     return x
# x = 0
# print(g(x))
# print(x)
