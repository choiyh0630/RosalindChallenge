f = open('Sample_Creating_a_Distance_Matrix.txt', 'r')
#f = open('rosalind_pdst.txt', 'r')
l = f.read().splitlines()

d = {}
for s in l:
    if s.startswith('>'):
        name = s[1:]
        d[name] = ''
    elif not s.startswith('>'):
        d[name] += s

# p-distance: proportions of corresponding symbols that differ in s1 and s2

def p_matrix(dic):
    for id1 in dic.keys():
        print(get_row_of_p_dist(id1, dic))

def get_row_of_p_dist(id1, dic):
    p_dist_row = ''
    for id2 in dic.keys():
        p_dist_row += ' ' + str(p_dist(id1, id2, dic))
    return p_dist_row[1:]

def p_dist(id1, id2, dic):
    s1 = dic[id1]
    s2 = dic[id2]
    # -- code 1: using for loop
    # divisor = len(s1)
    # dividend = 0
    # for i in range(len(s1)):
    #     if s1[i] != s2[i]:
    #         dividend += 1
    # return dividend / divisor
    # -- code 2: using list comprehension
    return sum([s1[i] != s2[i] for i in range(len(s1))]) / len(s1)


p_matrix(d)

