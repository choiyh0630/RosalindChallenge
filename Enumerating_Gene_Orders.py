# "Synteny block" = collection of contiguous genes located on the same chromosome (traits provided by
# these genes are usually inherited together, violating Mendel's law of independent assortment).
# A pair of synteny blocks from 2 different species are not strictly identical, but for the sake of studying
# large-scale rearrangements, we consider them to be equivalent --> we can label each synteny block with
# a positive integer; when comparing 2 species' genomes/chromosomes, we then only need to specify the order of
# its numbered synteny blocks.

# Given: A positive integer n <= 7
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

# This is a Backtracking problem. There are 3 keys to backtracking:
# 1. Choices --> set of decisions to take (we can only choose 1 number)
# 2. Constraint --> the decisions are limited by set of constraints (we can only choose 1 number and cannot reuse this number)
# 3. Goal --> our goal of the problem (a list of all possible permutations)

number = 3

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
permutations = permutation(5)

# create the output file ('Output_Enumerating_Gene_Orders.txt') that contains the answer in the desired format
output = open('Output_Enumerating_Gene_Orders.txt', 'w+')
for item, line in enumerate(permutations):
    if item == 0:
        output.write(str(line))
        output.write("\n")
    else:
        for i in line:
            output.write(' '.join(str(x) for x in i))
            output.write("\n")
output.close()
