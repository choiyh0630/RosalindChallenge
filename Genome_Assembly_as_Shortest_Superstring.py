# Almost all humans share approximately 99.9% of the same nucleotides on the genome.
# After obtaining a large collection of reads from multiple copies of the same genome, the aim is to reconstruct the desired
# genome from these smaller pieces of DNA --> "fragment assembly"

# For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.
# By assumption of parsimony, a shortest possible superstring over a collection of reads serve as a candidate chromosome.

# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format, where there exists a
#        unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

f = open('rosalind_long.txt', 'r')
# f = open('Sample_Genome_Assembly_as_Shortest_Superstring.txt', 'r')
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
        overlaps[r_id] = 'N/A'

print(overlaps)


def long_substr(dna_list):
    substr = ''
    if len(dna_list) > 1 and len(dna_list[0]) > 0:
        for i in range(len(dna_list[0])):
            for j in range(len(dna_list[0]) - i + 1):
                if j > len(substr) and is_substr(dna_list[0][i:i+j], dna_list):
                    substr = dna_list[0][i:i+j]
    return substr

# takes in a substring pattern and the list of DNA sequences
# returns whether the substring pattern is a common substring in all sequences in the list
def is_substr(subs, dna_lst):
    if len(subs) < 1 or len(dna_lst) < 1:
        return False
    for dna in dna_lst:
        if subs not in dna:
            return False
    return True

def get_key_of_value(v):
    return list(overlaps.keys())[list(overlaps.values()).index(v)]

scs = ''
ids = []
count = 0
while len(ids) < len(d.keys()):
    if count == 0:
        head_id = get_key_of_value('N/A')
        following_id = get_key_of_value(head_id)
        head = d[head_id]
        following = d[following_id]
        overlap = long_substr([head, following])
        overlap_start = head.find(overlap)
        scs += head[:overlap_start]
        scs += overlap
        overlap_start = following.find(overlap)
        scs += following[overlap_start+len(overlap):]
        count += 1
        ids.append(head_id)
        ids.append(following_id)
    else:
        following_id = get_key_of_value(following_id)
        head_id = overlaps[following_id]
        overlap = long_substr([d[head_id], d[following_id]])
        overlap_start = d[following_id].find(overlap)
        scs += d[following_id][overlap_start+len(overlap):]
        ids.append(following_id)

# Output
print(scs)

