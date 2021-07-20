# War between bacteriophages (viruses that target bacteria) and bacteria
# To defend itself, bacteria employs restriction enzymes (operates by cutting through viral DNA to cripple the phage).
# Restriction enzyme is a homodimer (composed of two identical subtructures); both substructures are pre-programmed with the same target
# string containing 4 - 12 nucleotides to search for within the phage DNA.

# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12.

# f = open('rosalind_revp.txt', 'r')
# seq_lst = f.read().splitlines()[1:]
# seq = ''.join(seq_lst)
# print(seq)

seq = 'TCAATGCATGCGGGTCTATATGCAT'

