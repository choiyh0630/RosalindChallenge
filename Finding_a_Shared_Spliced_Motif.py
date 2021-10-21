from Bio import SeqIO
import numpy as np

# dnas = SeqIO.parse("./Sample_Finding_a_Shared_Spliced_Motif.fa", "fasta")
dnas = SeqIO.parse("./rosalind_lcsq.fa", "fasta")
dna_lst = []
for dna in dnas:
    dna_lst.append(str(dna.seq))
dna_lst = sorted(dna_lst, key=len, reverse=True)
s = dna_lst[0]
t = dna_lst[1]

print(dna_lst)


# Recursion
def LCS(s1, s2):
    if s1 == "" or s2 == "":
        return 0
    elif s1[-1] == s2[-1]:
        return 1 + LCS(s1[:-1], s2[:-1])
    else:
        return max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))

# Dynamic Programming
dp_table = np.zeros((len(s) + 1, len(t) + 1))

# to reflect the empty string in the dp table
# s = " " + s
# t = " " + t

for i in range(1, len(s)):
    for j in range(1, len(t)):
        if s[i] == t[j]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + 1
        else:
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

print(dp_table[-1][-1])

# Traverse the dp table to obtain the actual LCS string
i = len(s) - 1
j = len(t) - 1
lcs = ""
while dp_table[i][j] > 0:
# while i * j != 0:
    curr = dp_table[i][j]
    left = dp_table[i][j - 1]
    up = dp_table[i - 1][j]
    if up == curr:
        i -= 1
    elif left == curr:
        j -= 1
    else:
        lcs += s[i]
        i -= 1
        j -= 1

    # if left == up and dp_table[i-1][j-1] < dp_table[i][j]: --> this is wrong because you have to compare the current value to left or up, not just compare left and up
    #     lcs += s[i]
    #     i -= 1
    #     j -= 1
    # elif left > up:
    #     j -= 1
    # else:
    #     i -= 1
lcs = lcs[::-1]
print(lcs)
