# Mendel's second law = Law of Independent Assortment
# 2 events A and B are independent if P(A and B) = P(A) * P(B)

# Given: 2 positive integers k (k <= 6) and N (N <= 2^k). Tom (0th generation) has genotype AaBb.
#        Tom has 2 children in the 1st gen, each of whom has 2 children, and so on. Each organism
#        always mates with a genotype AaBb organism.
# Return: The probability that at least N AaBb organism will belong to the k-th generation of Tom's family tree.

# 1. We want to ultimately calculate = P(at least N AaBb organisms in k-th gen) = summation of p_i at kth gen. from i=N to i=2^k
# 2. Get recursive equation for p_i at kth gen --> try to find expression of p_i at kth gen in terms of p_i at k-1 gen.
# 3. Because no matter what genotype each offspring is, when it mates with AaBb, P(AaBb) = 1/4. We discover that P(i organisms are AaBb in kth gen | parents genotype) = P(i organisms are AaBb in kth gen)
#       p_i at kth gen ~ PMF of Binom(2^k, 1/4) because P(1 individual has AaBb) = Bern(1/4);
#           Then, p_i at kth gen = PMF of Binom(2^k, 1/4).

from scipy.stats import binom
N = 16
k = 6

def prob(N, k):
    p = 1/4
    # 1 - binom.cdf since it's tail summation
    # N - 1 because you take the complement of at least N == smaller than N
    return 1 - binom.cdf(N - 1, 2**k, p)
print(prob(N, k)) # 1 - binom.cdf since it's tail summation
