# A subsequence of a string is a collection of symbols contained in order (not necessarily contiguously in the string.
# A subsequence can have multiple collection of indeces.

# Given: Two DNA Strings s and t (each of length at most 1 kbp) in FASTA format.
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s.

f = open('rosalind_sseq.txt', 'r')
next = f.readline()
d = {}
while next != '':
    if next.startswith('>'):
        tmp = next[1:].strip('\n')
        d[tmp] = ''
        next = f.readline().strip('\n')
    d[tmp] += next
    next = f.readline().strip('\n')
print(d)

s = list(d.values())[0]
t = list(d.values())[1]
# s = 'ACGTACGTGACG'
# t = 'GTA'

indices = []
for i in range(len(t)):
    n = t[i]
    for id in range(len(s)):
        if n == s[id]:
            if i == 0:
                indices.append(id)
                break
            elif i > 0:
                if id < indices[i - 1] or abs(id - indices[i - 1] <= 1):
                    continue
                indices.append(id)
                break

print([idx + 1 for idx in indices])
