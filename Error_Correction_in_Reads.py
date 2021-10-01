from collections import Counter
# from collections import OrderedDict

f = open('./rosalind_corr.txt', 'r')
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

# input: a dictionary that has key:value pair of 'sequence identifier: read'.
# output: a dictionary that has key: value pair of 'old read: new read', where the old read is the incorrect read with
#         a point mutation and the new read is the correct read (or its reverse complement).
def get_error_corrections(reads_dic):
    corrections_result = {}
    original_reads = [read for read in reads_dic.values()]
    correct_reads_dic = get_correct_reads(original_reads)
    print(correct_reads_dic)
    correct_reads_lst = list(correct_reads_dic.keys()) + list(correct_reads_dic.values())

    # for each original read, check with all the correct reads to see if it's an incorrect read that has a single nucleotide mutation
    for read in correct_reads_lst:
        for original_read in original_reads:
            if is_Hamming_Distance_1(read, original_read):
                corrections_result[original_read] = read
    return corrections_result


# definition of a correct read = appears at least twice in the dataset, possibly as a reverse complement => get all the duplicates in the dataset
# input: a list that contains only the original reads
# output: a dictionary with a key: value pair of 'original read that are correct: its reverse complement'
def get_correct_reads(original_reads_lst):
    duplicates_in_original = {k: get_rev_comp(k) for k,v in Counter(original_reads_lst).items() if v > 1}
    rev_comp_lst = [get_rev_comp(read) for read in original_reads_lst]

    for read in original_reads_lst:
        for i in range(len(rev_comp_lst)):
            if read == rev_comp_lst[i]:
                duplicates_in_original[read] = original_reads_lst[i]

    return duplicates_in_original


# returns True if the Hamming Distance between read1 and read2 is 1
def is_Hamming_Distance_1(read1, read2):
    dist = get_Hamming_Distance(read1, read2)

    if dist == 1:
        return True
    # else:
    #     rev_comp_dist = get_Hamming_Distance(read1, get_rev_comp(read2))
    #     if rev_comp_dist == 1:
    #         return True

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
    for i in read[::-1]:
        if i == 'A':
            rev_comp += 'T'
        elif i == 'T':
            rev_comp += 'A'
        elif i == 'G':
            rev_comp += 'C'
        else:
            rev_comp += 'G'
    return rev_comp


print(get_error_corrections(d))

# removes all the pairs that contain the reverse complement as the old read
# def filter_original_reads(paired_dic, original_dic):
#     return {k: paired_dic[k] for k in paired_dic if k in original_dic.values()}

result = get_error_corrections(d)
print(result)

# save all the results in the output dictionary as old read -> new read format in a txt file
output = open('Output_Error_Correction_in_Reads.txt', 'w')
for k, v in result.items():
    output.write(k + '->' + v + '\n')
output.close()


# my first stab at the problem; the key was to realize that we have to compare the reads to only the CORRECT reads
'''
def error_corrections(reads_dic):
    corrections = {}
    reads = [v for v in reads_dic.values()]
    for i in range(len(reads)):
        read1 = reads[i]
        for read2 in reads[i+1:]:
            if is_Hamming_Distance_1(read1, read2):
                if read1 not in corrections or read2 not in corrections:
                    corrections[read1] = read2
    return corrections

# returns a dictionary where the key-value pairs are the single-nucleotide corrections of each other
def error_corrections(reads_dic):
    corrections = {}
    # check if there are any duplicates and return unique reads
    # unique_reads = [k for k, v in Counter(reads_dic.values()).items() if v == 1]
    reads = [v for v in reads_dic.values()]
    # rev_comp_reads = []
    # for read in reads:
    #     rev_comp_reads.append(get_rev_comp(read))
    #
    # reads.extend(rev_comp_reads)

    # for each read, check if there are pair matches as reverse complements
    # AND check for any read pairs that have Hamming Distance of 1
    for i in range(len(reads)):
        read1 = reads[i]
        for read2 in reads[i+1:]:
            # if is_reverse_comp(i, read): -- we don't even need to know if there are rev comp matches for the result
                # remove the pairs since we don't need them in the output

            # if we haven't already matched the sequence with another sequence, check for Hamming Distance
            # if (read1 not in corrections) or (read1 not in corrections.values()):
            if is_Hamming_Distance_1(read1, read2):
                if read1 not in corrections or read2 not in corrections:
                    corrections[read1] = read2
    # corrections = filter_original_reads(corrections, reads_dic)
    to_check_rev_comp_lst = reads.copy()
    already_paired_reads = list(corrections.keys()) + list(corrections.values())

    for read in already_paired_reads:
        print(read)
        to_check_rev_comp_lst.remove(read)
    to_check_rev_comp_no_dup_lst = [k for k, v in Counter(to_check_rev_comp_lst).items() if v == 1]
    print(f'to_check: {to_check_rev_comp_no_dup_lst}')
    # rev_comp_reads = set([get_rev_comp(read) for read in to_check_rev_comp_lst]) -- set not ideal because it doesn't keep the original list's order
    rev_comp_reads = [get_rev_comp(read) for read in list(OrderedDict.fromkeys(to_check_rev_comp_lst))]
    print(rev_comp_reads)
    for i in range(len(to_check_rev_comp_no_dup_lst)):
        read1 = to_check_rev_comp_no_dup_lst[i]
        j = 0
        while j < len(rev_comp_reads):
            read2 = rev_comp_reads[j]
            if is_Hamming_Distance_1(read1, read2):
                corrections[read1] = read2
                break
            j += 1

    return corrections
'''
