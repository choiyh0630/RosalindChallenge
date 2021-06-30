# Hamming distance, dH(s1, s1), between 2 strings having the same length = minimum number of symbol substitutions
# required to transform one string into the other. Hamming distance is simply the number of positions in the strings
# at which corresponding symbols differ between 2 strings.

# Given: 2 DNA strings s and t of equal length
# Return: The Hamming distance dH(s,t)

s = 'AGGTCTATATATGAACACAGTCGCGTTAAGACGGTCCGAGATATTTGCGTCTGCATGGTGGACTAGCCCCGTTGGTCTATCACACCATACAAATAGTATCCACTGAATCGCAACGACAAAAGGGCTATCGGTCTGCTTAGATCATTCCTCGTCTTGGTACAGCACTGAAATCTTGAATTGATATAGGTAGCCGGTTAGTCCAACGTCGCAGTTCCGTACATGGGGAAGTAGAACCCCCTCTAAGTGAGTACGGTACAAGGAGGCTTGACCGCGCGGGGTAGCGTAGTCCTGTTCTAGATAAATAAGCACATCGCTGCGGGCGTTGCTAACCTTGCCACGCCACCGTCGGCAGAGCTGATGGGACGATGCTGCTTACGATATCTACTACACATAAGACTTCAATCACGCGTTTCAGGTACCCAGTGCTGAGATCGCAGTGGCTTCATGTGTCTCACCACACGGTTGGTCAGAGTCCTTCCACCCTTATGTCATTATTACGATTACAGCAGATGATTTCTAGTGGGTTATAATACTTCGTCGGTAATATCTCTTGTCTTAAAACCAGCTGCTATGCTAGGCGGGGATCGAGGGCGACGTAATCACCGGGTGTTCTCAATGAAATATTTCCTCCGCATGTAACTACCGCCAGGTGCTGAGTCATTTCATTCTTGTGTTAAGGGTGTATAGCAAGCCCTGTGAGAGTAGGGAGTGTTAGGGTGCTCGACCTAGACATCTAGCCGTCAAGTATGGCTGCTCTACTTTAAATGGAGCCTGCTGACTCTGGGCAAGTTGGTAGATTCCGCCGTTGCCTCCGAGCTTAATGATCGTGTAAATAAGGGGGCTCGCTGCCGCCAGGTGACCGGTCAATCAAACCAGCCTTCCAAATAGTCCCTGAAAGAAAGTAGTACATGATCGTGGGAGTGCACGTAACGCGATACC'
t = 'AGGTCGTGTCTTGAACAGTGCCTACTACGCTCTGTATAGAATAGTAATGTTGTACTGAGGGTATAACCCACATTGTTTCTTACTCTGTTTAAATTTGAGAGAGGGGTAGTCCCCACAGAAATGCTCATTGATCTGCTTACATCATCTCGTAGCCTCGCAGCGTCCTGTTGCGTCGGAATGCTTTACGCACCAGAGCAATGCAAGGACGTAGACGTGCCGCTTGGCAATTATCTTCGCCGCAATGCGGTTACCTCACGGGGAGTCGTTGTGGGACGCGTTGGTTATTTCGACTTCTAGTTCATCACGTTCGTGGCAGACATTGTATCCAAGATTCCGCCAGCACCGAAGCGTTTGCTGTTTGTTCGAGGCTGTCTACCATTGCTCCTACCAAGATATCCTGATTTACGCATTACGCGTACCTATGCCGGAGATGCCACTAGGATCGAATATACTTCAAAACAGCTTGGGAGTGTCCTTTAACATGTGTCCAAGTTTTCCAATTTCAGAATATCACGTAATGAGCTGTGGGGGTCGGCAGTCGTAATCTCTCTTTGGCTCCGAGGGAATGCTTTGCTAGGCTAATACCTACGGTGCGGCATTCCCCAGGTATCATTACAGCGATACTTCCTTCACCGGGTACAACTGCCTATCTCTAGGTCATAGAATTATTAGGTCCGGTTCGCAGACCAAGCCTTGTCACCGTTGCTTAAGGCACGGTCGGCCTTGTAATCATGTGGGCCTAAAAGTGGTCTGCATTGAGTGACATTGTGTCCGATCGCTGAGCGAAAGTTAAGCGGTACTGCTGTAGTCCCCGACCTAAAAGGTTCGGCTAATACTCTAGATCTGTTGCGCCCGATAACCGGTGACTCACTCCCTGATTCCATGTCAGCCCCTAAAGAATAGTGTTCCAGGCTGTTGGTGCGATTGTAGCGATCAAAG'

count = 0
for n in range(len(s)):
    if s[n] != t[n]:
        count += 1

print(count)
