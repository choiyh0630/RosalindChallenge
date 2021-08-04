# Given 2 strings s and t having the same length n, we say that s precedes t in the lexicographic order if the first symbol
# s[j] that doesn't match t[j] satisfies s_j < t_j.

# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n <= 10).
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.

c = 'A C G T'
n = 2

print('B' > 'A')

def permutations(num, colxn):
    collection = colxn.split(' ')
    def permute(num):
        result = []
        if num == 0:
            return ['']
        for perm in permute(num - 1):
            for s in collection:
                result.append(perm + s)
        return result
    return permute(num)


# print(permutations(n, c))

# Iterative way
res = ['']
for i in range(2):
    temp = []
    for r in res:
        for s in c.split(' '):
            temp.append(r + s)
    res = temp
print(res)

