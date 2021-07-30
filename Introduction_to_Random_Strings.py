# What is the critical motif length at which we can throw out random chance and conclude that a motif appears in a genome
# for a reason?
# If the GC-content is x, then frequency of C and G = x/2; frequencies of A and T = (1-x)/2

# Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1
# Return: An array B having the same length as A in which B[k] represents the common logarithm (log_10(x)) of the probability
#         that a random string constructed with the GC-content found in A[k] will match s exactly.

# 1. Calculate P(G) and P(C) from array A
# 2. Calculate P(A) and P(T) from array T
# 3. Loop through the string to calculate the probability of generating string s by random chance
# 4. Convert the probability to common logarithmic form

import math

s = 'GGACGATTGCGTAATATTTAGGAGTACGAGCGTGTATACGACTACACGTGAACGCACGAGGCACCGTCGCTTGTATGCTTTAGTTCACTTCCA'
str_A = '0.099 0.130 0.220 0.291 0.316 0.396 0.485 0.550 0.593 0.670 0.720 0.788 0.852 0.883'
A = [float(x) for x in str_A.split(' ')]

def get_probabilities(p):
    p_g = p_c = p / 2
    p_a = p_t = (1 - p) / 2
    return [p_g, p_c, p_a, p_t]

def get_prob_dna_random_chance(dna_str, gcat_prob_arr):
    p_G, p_C, p_A, p_T = gcat_prob_arr
    prob = 1
    for nuc in dna_str:
        if nuc == 'G':
            prob *= p_G
        elif nuc == 'C':
            prob *= p_C
        elif nuc == 'A':
            prob *= p_A
        else:
            prob *= p_T
    return "{:.3f}".format(round(math.log(prob, 10), 3))

B = []
for P in A:
    B.append(get_prob_dna_random_chance(s, get_probabilities(P)))

# output result in the format Rosalind wants
result = ' '.join(B)
print(result)

# TO NOTE:
# Using the above algorithm (while it is probably good enough for the Rosalind datasets) you will get probability zero
# (and math error when computing the logarithm) for longer strings (try for example a string of 1000 random nucleotides).
# This is because the Python floating numbers cannot represent very small (but still positive) values - the smallest positive value
# is 2.2250738585072014e-308. Because of this, and because of the mathematical properties of the logarithm (log10(x⋅y)=log10(x)+log10(y)),
# it is much better to compute the logarithm of the probability of each consecutive base, and then add these values to get the final logarithm of probability.

def get_prob_dna_random_chance_additive(dna_str, gcat_prob_arr):
    """Probability is calculated by taking advantage of the additive property of log (log10(x⋅y)=log10(x)+log10(y))"""
    p_G, p_C, p_A, p_T = gcat_prob_arr
    prob = 0
    for nuc in dna_str:
        if nuc == 'G':
            prob += math.log(p_G, 10)
        elif nuc == 'C':
            prob += math.log(p_C, 10)
        elif nuc == 'A':
            prob += math.log(p_A, 10)
        else:
            prob += math.log(p_T, 10)
    return "{:.3f}".format(round(prob, 3))

B_additive = []
for P in A:
    B_additive.append(get_prob_dna_random_chance_additive(s, get_probabilities(P)))

print(B_additive)
print(B_additive == B) # Returns true since the DNA sequence provided is small and the additive function is working properly
