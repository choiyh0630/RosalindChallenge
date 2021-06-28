# In DNA strings, 'A' and 'T' are complements of each other, as a 'C' and 'G'
# The reverse complement of a DNA string is formed by reversing the string and taking the complement of each symbol.
# We must reverse the string in addition to taking complements because of the directionality of DNA:
# DNA replication and transcription occurs from the 3' end to the 5' end, and the 3' end of one strand is opposite from the 5' end of the complementary strand.

# Given a DNA string s, return the reverse complement s_c of s
# = = = = My solution = = = =
s = 'CTACGACTAACCCATAAAACTCAACACCTGGCCTAAGTTGAGCACATGACCCTAAAGAGCCCGCGTCTATTAGATTCAATGAAAAATCAATTGGCGTCACAGGAGACGTGCACTCTCTTAAATGTCACTGTGACGGTACCTCCCGAGTATCTGAACGACCCTACTAGCGGAAACATACGAGGCGGCGTACTAACCATCGAATGGCTATATATTCAGGTAGAACACAGGACGGTCTAGATAACCCTTCGCGGCTTTGCCTAACCTTGAGTCTTAGTCTTCTCACGCCTCTATTATAAAGTTGCCTAGTAGTCGTCAAAATTACCTCTATGCGACAAATACAAAGAAGAATCTATCTTCCTATCTTAATAACTTGACACTGAGGAAAGGATTTGTTGGACAGACGGTAAATGGCGTTATTTGAGAGGGGGTGATGTAGTCCCTCCGATGAAACCCCATTAGGCCGGAGCTGATGCGAAAGACATGAATACGTGAAAATGGAGATTGACAAAGCTCCTATGACTCAACCGCTAATGCTATGAACGACTTGGTGGGGATAGCACGTAGAATGCGCTTGCCAACTACAAGTTACCAACAGCCTTTTATTACGGATCAAGATTGCGCATCTTGGGTTGATACACTTTGTCTCCCAAGAAGCTCCCGGTGCTGATGGTGAAAGGGTATAATGGCGATTGAAGGGCTCAGACGAAAAAATCAGTCAATAGAAGTTGTCCCATGACCCTGGGCAGACCCACCCCGGTCGGTTAGGATCGACCTGTTCGATCAACGTCTAAATGCCCAAGGATCGGGCAAGGTATTTGTTGCGGCACCATCAATTATGGAAGAAGCTTGTTAAGGGAATTCGACTCGTGTAGTTACA'
reverse = s[::-1]
s_c = ''

for i in range(len(reverse)):
    if reverse[i] == 'A':
        s_c += 'T'
    elif reverse[i] == 'G':
        s_c += 'C'
    elif reverse[i] == 'C':
        s_c += 'G'
    else:
        s_c += 'A'

print(s_c)

# = = = = one-liner code from Rosalind Solutions = = = =
# translate method returns a string where some specified characters are replaced with the character described in a mapping table/dictionary.
# maketrans method creates a mapping table

s[::-1].translate(str.maketrans('ACGT', 'TGCA'))

