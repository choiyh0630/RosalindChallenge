# "Synteny block" = collection of contiguous genes located on the same chromosome (traits provided by
# these genes are usually inherited together, violating Mendel's law of independent assortment).
# A pair of synteny blocks from 2 different species are not strictly identical, but for the sake of studying
# large-scale rearrangements, we consider them to be equivalent --> we can label each synteny block with
# a positive integer; when comparing 2 species' genomes/chromosomes, we then only need to specify the order of
# its numbered synteny blocks.

# Given: A positive integer n <= 7
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

number = 3

def permutation(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# lst = []
# for i in range(1, 3 + 1):
#     l = []
#     for j in
