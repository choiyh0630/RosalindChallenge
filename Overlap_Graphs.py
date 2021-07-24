# Networks are prevalent for modeling the spread of disease in biology.
# Graph = technical term for a network. A graph is made up of hubs called nodes (or vertices), pairs of which are connected via
#         segments/curves called edges. If an edge connects nodes v and w, then it's denoted by v,w == w,v.
# An edge v,w is incident to nodes v and w = v and w are adjacent to each other
# Degree of v = # of edges adjacent (incident) to it
# Walk = ordered collection of edges for which the ending node of one edge is the starting node of the next (ex. {v1,v2}, {v2,v3}, {v3,v4})
# Path = walk in which every node appears in at most 2 edges.
# Path length = number of edges in the path
# Cycle = path whose final node is equal to its first node
# Distance between 2 vertices = length of the shortest path connecting them

# Adjacency list = 2 column matrix that represents the edge relations of a graph
# Directed graph = graph containing directed edges, each of which has an orientation. The starting and ending nodes of an edge form its tail and head, respectively.
#                  The directed edge with tail v and head w is represented by (v,w) but not by (w,v).
# Directed loop = directed edge of the form (v,v)
# For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph O_k, in which each string is represented by a node,
# and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s != t.
# Useful video about Overlap Graphs: https://www.youtube.com/watch?v=yPJ7yHRk2OI

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O_3.

k = 3
file = open('Sample_Overlap_Graphs.txt', 'r')
#file = open('rosalind_grph.txt', 'r')
reads = file.read().splitlines()
print(reads)

dna_dic = {}
i = 0
while i < len(reads):
    if reads[i].startswith('>'):
        id = reads[i][1:]
        dna_dic[id] = ''
        i += 1
    dna_dic[id] += reads[i]
    i += 1
print(dna_dic)

class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_lst = {}

        for n in self.nodes:
            self.adj_lst[n] = []

def is_prefix(suffix_seq, prefix_seq, threshold):
    suffix = suffix_seq[-threshold:]
    prefix = prefix_seq[:threshold]
    if suffix == prefix:
        return True
    return False

seq = "AAATAAA"
seq_2 = 'AAATTTT'
print(is_prefix(seq, seq_2, k))
