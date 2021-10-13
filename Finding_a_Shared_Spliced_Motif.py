from Bio import SeqIO

dnas = SeqIO.parse("./Sample_Finding_a_Shared_Spliced_Motif.fa", "fasta")
dna_lst = []
for dna in dnas:
    dna_lst.append(str(dna.seq))

s = dna_lst[0]
t = dna_lst[1]

print(dna_lst)

def LCS(s1, s2):
    if s1 == "" or s2 == "":
        return 0
    elif s1[-1] == s2[-1]:
        return 1 + LCS(s1[:-1], s2[:-1])
    else:
        return max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))

s = "abcde"
t = "bce"
print(LCS(s, t))
