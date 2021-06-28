# Given a DNA string s, return 4 integers counting the respective number of times that each nucleobases of DNA appears in s
s = 'CCTGAAAATATGTATTCAAGAGGTAAGGCCCAGCGTACTATAACCTACACCAAATGGCGACGTCGAGAATGAGGGTTTGTATATCAGCACCTTTTGCATATGTCGAGCAAGAAAAGGTAGCTCGTGATGGTAGGTATCTGGACGTAGCCCTGGACATACAAGCACATCGAGGACACTTAACATGCTGTTCCAACGGCCTACCCCATATGCGATGCCCACGGCTAGCTCTCACGCGATACCGAGCGGCTTACCGGCGGCCAGCAGCGCACTTTCCCAGCTCTATAAGACCGTTGCCGACAATGCCGATCTTAATTAAGGGAATCTGGAGCGAGCCTTAAACAACCAAATATTTCCACAATATCCAATGCTGAAACTAGGGCCAGCTGTAGTGGGCATTCCCCCCCTAGATCATCCTGCTTAGCCCACACTCCAGCATATAATCGACGGCGACAGCCATCTCGCGGTAAGCCATCGGCCTGTGCAACGTACAGAGTCTCGTCTGGTTTCCCTACATGTGCGAGGTAGTCCAATGAGGACGAGCTCCATTGCGCTCCTCTAACGGGAGACTGCTCCTGGCAACTCGCTAACCGTGTCTTACGAGAGGCCTTGCCATGCAAACGGTTCGATGCGTCCGATCGCTCATACACGATACCCGGGCGTCGCAACGATGTATTTATGCGTCTACTTGCTCTACGCGGGTGGTCACTAATGGGCTGGACACTTACTGATCATCGGCCTGGGGACCTATCAAGAGGGTCTGCGTATTAGTGGGTTCGTCCCGAAGAAACCTGCTTCGCCTCAGTTGTGGTAAAGCGTATCATCCATTCTACTTGGCAGCCGACCTTTGTATGAAGAATCGACACTCGCACGACGAATCAAGGCTGGCACTGCAAGACCCGATTCTCGAGCGCGCCCGAAATGTGTTCCTAGTTATATGTGGGTTGAGTAGTGCTGCCTCAAGGGTCCC'
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

# for key in sorted(d.keys()):
#     print(f'{key} {d[key]}')

for key in sorted(d.keys()):
    print(d[key])
