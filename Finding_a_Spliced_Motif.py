# A subsequence of a string is a collection of symbols contained in order (not necessarily contiguously in the string.
# A subsequence can have multiple collection of indeces.

# Given: Two DNA Strings s and t (each of length at most 1 kbp) in FASTA format.
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s.

s = 'ACGTACGTGACG'
t = 'GTA'

indices = []
for i in range(len(t)):
    n = t[i]
    for id in range(len(s)):
        if n == s[id]:
            if i == 0:
                indices.append(id)
                break
            elif i > 0:
                if id < indices[i - 1] or abs(id - indices[i - 1] == 1):
                    continue
                indices.append(id)
                break

print([idx + 1 for idx in indices])
