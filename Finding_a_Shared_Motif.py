# a longer shared motif among different genomes --> greater shared function

# Given: A collection of k (k <= 100) DNA strings of length at most 1 kbp each in FASTA format
# Return: A longest common substring of the collection (if multiple solutions exist, return any single solution).

f = open('Sample_Finding_a_Shared_Motif.txt', "r")
dna_lst = []
for line in f.read().splitlines():
    if line.startswith('>'):
        continue
    else:
        dna_lst.append(line)

print(dna_lst)
