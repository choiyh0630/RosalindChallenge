# Given: 6 non-negative integers, each of which does not exceed 20000. The integers correspond to
#        the number of couples in a population possessing each genotype pairing for a given factor.
# The genotypes of 6 pairs:
# 1. AA - AA
# 2. AA - Aa
# 3. AA - aa
# 4. Aa - Aa
# 5. Aa - aa
# 6. aa - aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation
#         assuming every couple has exactly 2 offspring.

a = 1
b = 0
c = 0
d = 1
e = 0
f = 1

def expectation(a, b, c, d, e, f):
    p_a = 1
    p_b = 1
    p_c = 1
    p_d = 3 / 4
    p_e = 1 / 2
    p_f = 0
    return (2*a)*p_a + (2*b)*p_b + (2*c)*p_c + (2*d)*p_d + (2*e)*p_e + (2*f)*p_f

print(expectation(16622, 17666, 19917, 16640, 16117, 19166))
