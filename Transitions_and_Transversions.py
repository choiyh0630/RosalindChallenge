# 2 types of point mutations in DNA: transitions and transversions.
# Transition: Substitutes 1 purine for another (A <--> G) or 1 pyrimidine for another (C <--> T); a transition does not change
#             the structure of the nucleobase.
# Transversion: Interchange of a purine for a pyrimidine base or vice versa.
# Transversions require a more drastic change to the base's chemical structure --> less common than transitions
# Across entire genome, the ratio is about 2:1, but in coding regions, this ratio is typically higher (often exceeds 3)
# because a transition appearing in coding regions happens to be less likely to change the encoded amino acid, esp. when the
# substituted base is the 3rd member of a codon (silent substitution). This ratio of transitions to transversions therefore
# can be used for potentially identifying coding DNA in genomes.

# Hamming distance = Minimum number of symbol substitutions required to transform 1 string into the other; simply, the
#                    number of positions in the strings at which corresponding symbols differ.
# Given: 2 DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: The transition/transversion ratio R(s1, s2)

f = open('rosalind_tran.txt', 'r')
lst = f.read().splitlines()
print(lst)

dna_dic = {}
i = 0
while i < len(lst):
    if lst[i].startswith('>'):
        id = lst[i][1:]
        dna_dic[id] = ''
        i += 1
    dna_dic[id] += lst[i]
    i += 1
print(dna_dic)

print(dna_dic.values())
seq1 = list(dna_dic.values())[0]
seq2 = list(dna_dic.values())[1]
# seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
# seq2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'

transition = 0
transversion = 0
for n in range(len(seq1)):
    s1 = seq1[n]
    s2 = seq2[n]
    if s1 != s2:
        if s1 in ('A', 'G') and s2 in ('A', 'G'):
            transition += 1
        elif s1 in ('C', 'T') and s2 in ('C', 'T'):
            transition += 1
        else:
            transversion += 1
# Answer
print(transition / transversion)

