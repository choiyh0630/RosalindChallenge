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
print(seq)
#rev_c = ''

def reverse_complement(sequence):
#    rev = sequence[::-1]
    s = ''
    for n in sequence:
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

# dic = {}
# for i_s in range(len(seq)):
#     pal = ''
#     i_r = len(seq) - 1 - i_s
#     # print(i_s)
#     # print(i_r)
#     if seq[i_s] == rev_c[i_r]:
#         if i_s not in dic:
#             temp = i_s
#             dic[i_s] = ''
#         dic[temp] += seq[i_s]
# print(dic)

#print(rev_c[3+3:3+12])
dic = {}
for i in range(len(seq)):
    print(i)
    if i + 4 > len(seq):
        continue
    rev_range = rev_c[i+3:i+12]
    if seq[i] in rev_range:
        locs_rev = [loc for loc, n in enumerate(rev_range) if n == seq[i]]
        for l in locs_rev:
            temp_i = i
            pal = ''
            while not l < i and rev_c[l] == seq[temp_i]:
                if 4 <= len(pal) <= 12 and i not in dic:
                    dic[i] = ''
                pal += seq[temp_i]
                l -= 1
                temp_i += 1
            if 4 <= len(pal) <= 12:
                    dic[i] = pal
print(dic)
# dic = {}
# for i in range(len(seq)):
#     l = r = i
#     s = ''
#     while l >= 0 and r < len(seq) and seq[l] == seq[r]:
#         s = seq[l] + s + seq[r]
#         l -= 1
#         r += 1
#     if 4 <= len(s) <= 12:
#         dic[i] = s
# for i in range(len(seq)):
#     l = i
#     r = i+1
#     s = ''
#     while l >= 0 and r < len(seq) and seq[l] == seq[r]:
#         print(l)
#         s = seq[l] + s + seq[r]
#         l -= 1
#         r += 1
#     if 4 <= len(s) <= 12:
#         dic[i] = s
#
# print(dic)
# a = 'a'
# b = 'b'
# s = 's'
#
# s = a + s
# s = s + b
# print(s)
#
# if 0 <= len(s) <= 1:
#     print(s)
