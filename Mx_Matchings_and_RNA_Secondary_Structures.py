f = open('rosalind_mmch.txt', 'r')
lst = f.read().splitlines()
s = ''
for i in lst:
    if i.startswith('>'):
        continue
    s += i

# s = 'CAGCGUGAUCAC'

# comb(more, less) * factorial(less)

def total_number_of_ways(rna):
    au_pairs = get_number_of_pairs(rna, 'AU')
    gc_pairs = get_number_of_pairs(rna, 'GC')
    if au_pairs == 0 and gc_pairs == 0:
        return 0
    if au_pairs == 0:
        au_pairs = 1
    if gc_pairs == 0:
        gc_pairs = 1
    return au_pairs * gc_pairs

def get_number_of_pairs(rna, nuc_pair):
    if nuc_pair == 'AU':
        n_purine = get_number_of_nuc(rna, 'A')
        n_pyrimidine = get_number_of_nuc(rna, 'U')
    elif nuc_pair == 'GC':
        n_purine = get_number_of_nuc(rna, 'G')
        n_pyrimidine = get_number_of_nuc(rna, 'C')
    bigger = max(n_purine, n_pyrimidine)
    smaller = min(n_purine, n_pyrimidine)
    return comb(bigger, smaller) * factorial(smaller)

def get_number_of_nuc(rna, nucleotide):
    count = 0
    for nuc in rna:
        if nuc == nucleotide:
            count += 1
    return count

def comb(n1, n2):
    return int(factorial(n1) / (factorial(n2) * factorial(n1-n2)))

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

print(s)
print(total_number_of_ways(s))

