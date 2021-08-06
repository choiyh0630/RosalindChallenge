# Almost all humans share approximately 99.9% of the same nucleotides on the genome.
# After obtaining a large collection of reads from multiple copies of the same genome, the aim is to reconstruct the desired
# genome from these smaller pieces of DNA --> "fragment assembly"

# For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.
# By assumption of parsimony, a shortest possible superstring over a collection of reads serve as a candidate chromosome.

# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format, where there exists a
#        unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

f = open('Sample_Genome_Assembly_as_Shortest_Superstring.txt', 'r')
l = f.read().splitlines()
d = {}
i = 0

while i < len(l):
    if l[i].startswith('>'):
        id = l[i][1:]
        d[id] = ''
        i += 1
    d[id] += l[i]
    i += 1

print(d)

half_len = len(list(d.values())[0]) // 2
#print(list(d.values())[0][:half_len+1])

overlaps = {}
for r_id, read in d.items():
    found_overlap = False
    for r_id_2, read_2 in d.items():
        if r_id != r_id_2:
            if read[:half_len+1] in read_2:
                overlaps[r_id] = r_id_2
                found_overlap = True
    if not found_overlap:
        overlaps[r_id] = None

print(overlaps)
