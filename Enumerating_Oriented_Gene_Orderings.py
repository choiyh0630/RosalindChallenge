# Synteny block = a collection of contiguous genes located on the same chromosome. Traits provided by these gens are usually
#                 inherited together, thus violating Mendel's law of independent assortment.
# Each strand of a DNA molecule has an orientation, and so we should provide each synteny block with an orientation to indicate
# the strand on which it is located.

# Signed permutation of length n = an ordering of the first n positive integers in which each integer is then provided with either
#                                  a + / - sign.
# Given: A positive integer n <= 6
# Return: The total number of signed permutations of length n, followed by a list of all such permutations.

from itertools import product

number = 4

def permutation(num):
    lst = list(range(1, num+1))
    permutations = permute(lst)
    return len(permutations), permutations

def permute(lst):
    result = []
    # base case
    if len(lst) == 1:
        return [lst[:]]

    for i in range(len(lst)):
        v = lst[i]
        # recursive call
        perms = permute(lst[:i]+lst[i+1:])
        # append the ith element to the permutations generated
        for perm in perms:
            perm.append(v)
        # update the overall list of permutations
        result.extend(perms)

    return result

# Rosalind given number = 5
permutations = permutation(number)
print(permutations)

def orientation_perm(perms):
    # Generate + and - of each number
    # Obtain the cartesian product of all +/- of each number
    return list(product(*([x, -x] for x in perms)))

lst = []
for i in permutations[1]:
    lst.extend(orientation_perm(i))

print(len(lst))
for tup in lst:
    print(*tup)
