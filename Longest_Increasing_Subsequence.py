# A subsequence of a permutation is a collection of elements of the permutation in the order they appear. For example, (5,3,4)
# is a subsequence of (5,1,3,4,2). A subsequence is increasing if the elements of the subsequence increase, and decreasing if the
# elements decrease. For example, given the permutation (8,2,1,6,5,7,4,3,9), an increasing subsequence is (2,6,7,9), and a decreasing
# subsequence is (8,6,5,4,3)

# Given: A positive integer n <= 10000 followed by a permutation pi of length n.
# Return: A longest increasing subsequence of pi, followed by a longest decreasing subsequence of pi.

n = 5
pi = '5 1 2 4 3'
pi_2 = '5 1 4 2 3'
pi_lst = pi.split(' ')
print(pi_lst)

d = {}
for i in range(len(pi_lst)):
    d[pi_lst[i]] = pi_lst[i]
    for j in pi_lst[i+1:]:
        tmp = d[pi_lst[i]][-1]
        if int(d[pi_lst[i]][-1]) < int(j):
            d[pi_lst[i]] += ' ' + j
        elif int(d[pi_lst[i]][-1]) > int(j) and int(pi_lst[i]) < int(j):
            d[pi_lst[i]] = d[pi_lst[i]][:-1] + j

print(d)

d_dec = {}
for i in range(len(pi_lst)):
    d_dec[pi_lst[i]] = pi_lst[i]
    for j in pi_lst[i+1:]:
        tmp = d_dec[pi_lst[i]][-1]
        if int(d_dec[pi_lst[i]][-1]) > int(j):
            d_dec[pi_lst[i]] += ' ' + j
        elif int(d_dec[pi_lst[i]][-1]) < int(j) and int(pi_lst[i]) > int(j):
            d_dec[pi_lst[i]] = d_dec[pi_lst[i]][:-1] + j

print(d_dec)
