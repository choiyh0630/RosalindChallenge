# Given: 3 positive integers: k, m, n
# population contains k + m + n organisms
# k individuals are homozygous dominant (AA) for a factor
# m are heterozygous (Aa)
# n are homozygous recessive (aa)

# Return: the probability that 2 randomly selected mating organisms will produce an individual possessing a
#         dominant allele. Assume that any two organisms can mate.

# P(A) = probability of offspring with at least 1 dominant allele
# Have to condition on the probability of getting each possible combination of parents
# Get the 1 - complement of the probability of getting offspring with no dominant alleles = 1 - P(A_c)
# It's only possible to obtain offsprings with no dominant alleles if the parents are:
# 1. both heterozygous
# 2. 1 heterozygous, 1 homozygous recessive
# 3. both homozygous recessive
# Condition on these 3 cases to calculate P(A_c)

def calculate_prob_dominant_allele(k, m, n):
    pop = k+m+n
    prob_het_het = (m / (pop)) * ((m-1)/(pop-1)) * (1/4)
    prob_het_rec = 2 * ((m / (pop)) * (n/(pop-1))) * (1/2) # have to multiply by 2 to account for getting parent pair (m,n) or (n,m)
    prob_rec_rec = (n / (pop)) * ((n-1)/(pop-1)) * 1

    return 1 - (prob_het_het + prob_het_rec + prob_rec_rec)

print(calculate_prob_dominant_allele(27, 24, 21))
