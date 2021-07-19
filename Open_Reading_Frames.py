# Open Reading Frame (ORF) = starts from the start codon and ends by stop codon, without any other stop codons in between.

# Given: A DNA string s of length at most 1 kbp (kilobasepair = 1000 base pairs in a DNA string) in FASTA format
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Can be returned in any order.

# The output should be all sequences that start with ATG (start codon) AND explicitly end with a Stop codon (TAA, TGA, TAA).
# Try all starting points; if no Stop codon found even when end of the string is reached, don't include it in output

import re

dna_codon_table = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
                   'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
                   'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
                   'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
                   'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
                   'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
                   'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
                   'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
                   'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
                   'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
                   'TAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
                   'TAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
                   'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
                   'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
                   'TGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
                   'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
                   }
# Read in the input file to obtain the DNA string
f = open('rosalind_orf.txt', 'r')
seq = f.read().splitlines()[1:]
seq = ''.join(seq)
print(seq)

# return the reverse complement strand of the original strand
def reverse_complement(dna):
    seq_c = ''
    for n in seq[::-1]:
        if n == 'A':
            seq_c += 'T'
        elif n == 'G':
            seq_c += 'C'
        elif n == 'C':
            seq_c += 'G'
        else:
            seq_c += 'A'
    return seq_c

seq_c = reverse_complement(seq)
print(seq_c)

# return a list of all possible candidate protein sequences from DNA string s
def dna_to_protein(s):
    proteins = []
    pattern = '(?=(ATG))'
    locs = [n.start() for n in re.finditer(pattern, s)]

    for loc in locs:
        sequence = s[loc:]
        p = ''
        for i in range(0, len(sequence), 3):
            if i+3 > len(sequence):
                #p = ''
                break
            else:
                codon = sequence[i:i+3]
                aa = dna_codon_table[codon]
                if aa == '*':
                    proteins.append(p)
                    break
                else:
                    p += aa

    return proteins

result = dna_to_protein(seq)
revc_protein = dna_to_protein(seq_c)

# Return all the possible proteins from reverse complement and original strand
result.extend(p for p in revc_protein if p not in result)
result_set = set(result) # remove duplicate protein sequences
print(result_set)

output = open('Output_Open_Reading_Frames.txt', 'w+')
for candidate in result_set:
    output.write(candidate + '\n')
output.close()

