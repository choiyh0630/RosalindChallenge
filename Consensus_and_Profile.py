# If we have a collection of DNA strings of length n each --> Profile matrix = 4 x n matrix P in which P_1,j represents the
# number of times that 'A' occurs in the jth position of one of the strings.
# Consensus string = string of length n formed from the collection of DNAs by taking the most common symbol at each position

# Given: A collection of at most 10 DNA strings of equal length in FASTA format
# Return: A consensus string and profile matrix for the collection.

# 1. Read in the FASTA file
# 2. Obtain just the DNA strings
# 3. Start with an empty matrix 4 x n
# 4. Loop through each string, updating the matrix with the count value
# 5. Return the consensus string + profile matrix

import numpy as np

# read in the file to obtain the DNA sequences
f = open('Sample_Consensus_and_Profile.txt', 'r')
lines = f.readlines()

dna_lst = []
new = False
dna = ''
for l in lines:
    if l.startswith('>') and dna == '':
        new = True
        continue
    elif l == lines[-1]:
        dna += l[:-1]
        dna_lst.append(dna)
    elif not l.startswith('>') and new:
        dna += l[:-1]
    elif l.startswith('>') and dna != '':
        dna_lst.append(dna)
        dna = ''

# Since all DNA sequences are of equal length, get the length of the first DNA sequence
dna_len = len(dna_lst[0])

# build an empty p matrix
p = np.zeros((4, dna_len))

# fill in the p matrix with the appropriate counts
for i in range(dna_len):
    for dna in dna_lst:
        if dna[i] == 'A':
            p[0][i] += 1
        elif dna[i] == 'C':
            p[1][i] += 1
        elif dna[i] == 'G':
            p[2][i] += 1
        else:
            p[3][i] += 1
print(p)

# build the consensus string based on the p matrix
c = ''
n_lst = ['A', 'C', 'G', 'T']
for i in range(dna_len):
    temp = 0
    loc = 0
    for n in range(4):
        if p[n][i] > temp:
            temp = p[n][i]
            loc = n
    c += n_lst[loc]
print(c)

# write the output to a file
output = open('Output_Consensus_and_Profile.txt', 'w+')
output.write(c + '\n')
for idx, l in enumerate(p):
    if idx == 0:
        output.write('A: ')
    elif idx == 1:
        output.write('C: ')
    elif idx == 2:
        output.write('G: ')
    else:
        output.write('T: ')
    output.write(' '.join(str(int(i)) for i in l) + '\n')

