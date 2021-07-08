# After identifying the exons and introns of an RNA string, we need to delete the introns and concatenate
# the exons to form a new string ready for translation.

# Given: A DNA string s and a collection of substrings of s acting as introns (in FASTA format).
# Return: A protein string resulting from transcribing and translating the exons of s.

# read in the file to obtain the DNA string and the intron patterns
f = open('rosalind_splc.txt', "r")
lst = f.read().splitlines() # Get rid of the newline symbol

# Create a dictionary of with key: sequence ID, value: DNA strand or intron
l = {}
for line in lst:
    if line.startswith('>'):
        id = line[1:]
        l[id] = ''
    elif l[id] == '':
        l[id] = line
    else:
        l[id] = l[id] + line

print(l)
l = list(l.values())

s = l[0]
introns = l[1:]
print(introns)

# splice the introns from the pre-mRNA
for intron in introns:
    exon = s.replace(intron, '')
    s = exon

print(exon)

def transcription(ex):
    return ex.replace('T', 'U')

# transcribe the mRNA
mrna = transcription(exon)

codon_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
               'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
               'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
               'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
               'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
               'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
               'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
               'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
               'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
               'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
               'UAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
               'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
               'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
               'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
               'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
               'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
               }

# translate the mRNA to protein
codons = [mrna[i:i+3] for i in range(0, len(mrna), 3)]
protein = ''
for codon in codons:
    p = codon_table[codon]
    protein += p

protein = protein[:-1] # get rid of Stop codon ('*')
print(protein)
