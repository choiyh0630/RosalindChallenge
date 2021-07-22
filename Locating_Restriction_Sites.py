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

# seq = 'TCAATGCATGCGGGTCTATATGCAT'
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

final = {}
for n in range(len(seq)):
    for i in range(4,12):
        sub = seq[n: n+i]
        rev_sub = reverse_complement(sub)
        if len(sub) >= 4 and sub == rev_sub:
            final[n + 1] = len(sub)
print(final)


# dic = {}
# for i in range(len(seq)):
#     if i + 4 > len(seq):
#         continue
#     rev_range = rev_c[i+3:i+12]
#     if seq[i] in rev_range:
#         locs_rev = [loc for loc, n in enumerate(rev_range) if n == seq[i]]
#         for l in locs_rev:
#             l += 3
#             temp_i = i
#             pal = ''
#             rev = rev_c[l+i]
#             seq_v = seq[temp_i]
#             while not l+i < i and rev_c[l+i] == seq[temp_i]:
#                 if 4 <= len(pal) <= 12 and i not in dic:
#                     dic[i] = ''
#                 pal += seq[temp_i]
#                 l -= 1
#                 temp_i += 1
#             if 4 <= len(pal) <= 12:
#                     dic[i] = pal
# print(dic)
# final = {key+1: len(value) for key, value in dic.items()}
# print(final)

output = open('Output_Locating_Restriction_Sites.txt', 'w+')
for key, value in final.items():
    output.write(str(key) + ' ')
    output.write(str(value) + '\n')
output.close()

