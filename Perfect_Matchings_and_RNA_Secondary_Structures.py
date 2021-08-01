# Just like DNA, even though RNA is single-stranded, the base pairs still bond to each other (A-U, and G-C). The base pairing
# interactions of an RNA molecule causes it to twist around itself (RNA folding). A hairpin loop is formed when consecutive
# elements from 2 different regions of an RNA molecule base pair. The same RNA molecule may base pair differently at different
# points in time, adopting many different secondary structures.

# A matching in a graph G is a collection of edges of G for which no node belongs to more than 1 edge in the collection.
# If G contains an even number of nodes (2n), then a matching on G is "perfect" if it contains n edges.
# K_n = complete graph on 2n labeled nodes, in which every node is connected to every other node with an edge.
# p_n = total number of perfect matchings in K_n = (2n-1)(2n-3)(2n-5)...(3)(1)
# Given an RNA string s = s1,...,sn, a bonding graph for s is formed as follows:
# 1. Assign each symbol of s to a node, and arrange these nodes in order around a circle, connecting them with adjacency edges.
# 2. Form all possible edges {A, U}, and {C, G}, called basepair edges. This represents a possibility for base pairing interactions in s.
# For a base pairing matching to exist, s must have the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' and 'G'.

# Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of
#        occurrences of 'C' as 'G'.
# Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

f = open('rosalind_pmch.txt', 'r')
lst = f.read().splitlines()
s = ''
for i in lst:
    if i.startswith('>'):
        continue
    s += i
print(s)

at_count = 0
gc_count = 0
for n in s:
    if n == 'A':
        at_count += 1
    elif n == 'G':
        gc_count += 1

at_comb = 1
gc_comb = 1
for x in range(1, at_count + 1):
    at_comb *= x
for y in range(1, gc_count + 1):
    gc_comb *= y
print(at_comb * gc_comb)

# class Graph:
#     def __init__(self, Nodes):
#         self.nodes = Nodes
#         self.edges = {}
#
#         for i in self.nodes:
#             self.edges[i] = []
#
#     def add_bp_edge(self, v, w):
#         self.edges[v].append(w)
#
# s = 'AGCUAGUCAU'
# s_lst = [s[i] + str(i) for i in range(len(s))]
# K = Graph(s_lst)
# print(K.edges)
#
# basepairs = {'A': 'U',
#              'U': 'A',
#              'G': 'C',
#              'C': 'G'
#              }
#
# for n in s_lst:
#     nuc1 = n[0]
#     idx1 = int(n[1:])
#     for x in s_lst:
#         if n == x:
#             continue
#         else:
#             nuc2 = x[0]
#             idx2 = int(x[1:])
#             if basepairs[nuc1] == nuc2 and n not in K.edges[x]:
#                 if abs(idx1 - idx2) == 1 or abs(idx1 - idx2) == len(s) - 1:
#                     continue
#                 else:
#                     K.add_bp_edge(n, x)
#
# print(K.edges)
