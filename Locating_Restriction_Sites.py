# War between bacteriophages (viruses that target bacteria) and bacteria
# To defend itself, bacteria employs restriction enzymes (operates by cutting through viral DNA to cripple the phage).
# Restriction enzyme is a homodimer (composed of two identical subtructures); both substructures are pre-programmed with the same target
# string containing 4 - 12 nucleotides to search for within the phage DNA.

# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12.

f = open('rosalind_revp.txt', 'r')
seq_lst = f.read().splitlines()[1:]
seq = ''.join(seq_lst)
print(seq)

# seq = 'TATATATATATA'
# print(seq)


def reverse_complement(sequence):
    s = ''
    for n in sequence[::-1]:
        if n == 'A':
            s += 'T'
        elif n == 'G':
            s += 'C'
        elif n == 'C':
            s += 'G'
        else:
            s += 'A'
    return s

rev_c = reverse_complement(seq)
print(rev_c)

final = []
for n in range(len(seq)):
    for i in range(4,13): # reverse palindrome has to be length between 4 and 12
        sub = seq[n: n+i]
        rev_sub = reverse_complement(sub)
        if n+i <= len(seq) and sub == rev_sub:
            final.append((n+1, len(sub)))

print(final)

output = open('Output_Locating_Restriction_Sites.txt', 'w+')
for pair in final:
    output.write(str(pair[0]) + '\t')
    output.write(str(pair[1]) + '\n')
output.close()

