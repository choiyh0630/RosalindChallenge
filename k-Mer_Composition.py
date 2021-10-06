from Bio import SeqIO

# using read(), not parse() because we're only expecting 1 DNA string; parse() returns an iterator
s = SeqIO.read("rosalind_kmer.fa", "fasta").seq
print(s)


def get_4mer_composition(dna):
    fmer_composition = [0 for i in range(256)]
    nuc_dic = {"A": 0, "C": 1, "G": 2, "T": 3}
    def get_4mer_index(fmer, nuc_mapping):
        index = 0
        quat_rep = {0: 4**3, 1: 4**2, 2: 4**1, 3: 4**0}
        for n in range(len(fmer)):
            index += quat_rep[n] * nuc_mapping[fmer[n]]
        return index

    for m in range(len(dna[:-3])):
        current_fmer = dna[m:m+4]
        fmer_pos = get_4mer_index(current_fmer, nuc_dic)
        fmer_composition[fmer_pos] += 1

    return fmer_composition

output = open("Output_k-Mer_Composition.txt", "w")
for count in get_4mer_composition(s):
    output.write(str(count) + " ")

