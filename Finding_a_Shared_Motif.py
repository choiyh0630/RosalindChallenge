# a longer shared motif among different genomes --> greater shared function

# Given: A collection of k (k <= 100) DNA strings of length at most 1 kbp each in FASTA format
# Return: A longest common substring of the collection (if multiple solutions exist, return any single solution).

f = open('rosalind_lcsm.txt', "r")
dna_lst = []
is_dna = False
dna = ''
for line in f.read().splitlines():
    if line.startswith('>') and not is_dna:
        is_dna = True
        continue
    elif is_dna and not line.startswith('>'):
        dna += line
    if line.startswith('>') and is_dna:
        dna_lst.append(dna)
        is_dna = False
        dna = ''

dna_sorted = sorted(dna_lst, key=len)

# takes in a list of DNA sequences
# returns the longest common substring in the list of DNA sequences
def long_substr(dna_list):
    substr = ''
    if len(dna_list) > 1 and len(dna_list[0]) > 0:
        for i in range(len(dna_list[0])):
            for j in range(len(dna_list[0]) - i + 1):
                if j > len(substr) and is_substr(dna_list[0][i:i+j], dna_list):
                    substr = dna_list[0][i:i+j]
    return substr

# takes in a substring pattern and the list of DNA sequences
# returns whether the substring pattern is a common substring in all sequences in the list
def is_substr(subs, dna_lst):
    if len(subs) < 1 or len(dna_lst) < 1:
        return False
    for dna in dna_lst:
        if subs not in dna:
            return False
    return True

print(long_substr(dna_sorted))

