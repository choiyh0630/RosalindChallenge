l = 'F M Z L C X P A K R'
n = 4
# l = 'D N A'
# n = 3
l = l.split(' ')

def get_all_possible_seqs(n):
    # if n == 0:
    #     return []
    if n == 1:
        return l
    else:
        return get_next_set_of_seqs(get_all_possible_seqs(n-1), n-1)

def get_next_set_of_seqs(seq_lst, m):
    res = []
    # if not seq_lst: # when n == 1, seq_lst is [] because
    #     for i in l:
    #         res.append(i)
    #else:
    for s in seq_lst:
        res.append(s)
        if len(s) == m:
            for i in l:
                res.append(s + i)
    return res

#print(get_all_possible_seqs(n))
for i in get_all_possible_seqs(n):
    print(i)

output = open('Output_Ordering_Strings_of_Varying_Length_Lexicographically.txt', 'w')
for i in get_all_possible_seqs(n):
    output.write(str(i) + "\n")
