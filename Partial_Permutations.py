# A partial permutation is an ordering of only k objects taken from a collection containing n objects (i.e. k <= n).
# P(n, k) counts the total number of partial permutations of k objects that can be formed from a collection of n objects.

# Given: Positive integers n and k such that 100 >= n > 0 and 10 >= k > 0
# Return: The total number of partial permutations P(n, k), modulo 1000000.

# P(n, k) = n! / (n-k)!
import functools

n = 99
k = 9

def permutation(n, k):
    f = [i for i in range(n+1)][1:]
    x = n - k
    return functools.reduce(lambda a,b: a*b, f[x:]) % 1000000

print(permutation(n, k))
