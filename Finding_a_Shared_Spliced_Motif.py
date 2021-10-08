from Bio import SeqIO

dnas = SeqIO.parse("./Sample_Finding_a_Shared_Spliced_Motif.fa", "fasta")
for dna in dnas:
    print(dna.seq)
