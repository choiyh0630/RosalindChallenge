from Bio import SeqIO

dna = SeqIO.read('./Sample_Speeding_Up_Motif_Finding.fa', 'fasta')
s = dna.seq

failure_arr = [0]

j = 0
for i in range(1, len(s)):
    if s[i] == s[j]:
        failure_arr.append(j + 1)
        j += 1
    else:
        while j != 0:
            j = failure_arr[j - 1]

        # when j = 0
        failure_arr.append(0)






