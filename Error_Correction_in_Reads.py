from collections import Counter

f = open('./Sample_Error_Correction_in_Reads.txt', 'r')
l = f.read().splitlines()
print(l)
d = {}
for i in l:
    if i.startswith('>'):
        d[i[1:]] = ''
        key = i[1:]
    else:
        d[key] = i

print(d)

print(Counter(d.values()))
print([k for k, v in Counter(d.values()).items() if v == 1])

# returns a dictionary where the key-value pairs are the single-nucleotide corrections of each other
def error_corrections(reads_dic):
    corrections = {}
    # check if there are any duplicates and return unique reads
    unique_reads = [k for k, v in Counter(reads_dic.values()).items() if v == 1]

    # for each read, check if there are pair matches as reverse complements
    # AND check for any read pairs that have Hamming Distance of 1
    for i in range(len(unique_reads)):
        read1 = unique_reads[i]
        for read2 in unique_reads[:i] + unique_reads[i+1:]:
            # if is_reverse_comp(i, read): -- we don't even need to know if there are rev comp matches for the result
                # remove the pairs since we don't need them in the output

            # if we haven't already matched the sequence with another sequence, check for Hamming Distance
            if (read1 not in corrections) or (read1 not in corrections.values()):
                if is_Hamming_Distance_1(read1, read2):
                    corrections[read1] = read2

    return corrections

# returns True if the Hamming Distance between read1 and read2 is 1
def is_Hamming_Distance_1(read1, read2):
    dist = get_Hamming_Distance(read1, read2)

    if dist == 1:
        return True
    else:
        rev_comp_dist = get_Hamming_Distance(read1, get_rev_comp(read2))
        if rev_comp_dist == 1:
            return True

    return False

# calculates the Hamming Distance
def get_Hamming_Distance(read1, read2):
    dist = 0
    #read1 and read2 are of equal length as specified in the problem
    for i in range(len(read1)):
        if read1[i] != read2[i]:
            dist += 1
    return dist

# outputs the reverse complement of the input read
def get_rev_comp(read):
    rev_comp = ''
    return rev_comp

print(error_corrections(d))
# def is_reverse_comp(read1, read2):
#
#     return True



#
# for i in range(len(d.values())):
#     for j in list(d.values())[:i] + list(d.values())[i+1:]:
#         print(i, j)
