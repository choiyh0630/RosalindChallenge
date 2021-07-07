# Residue = a molecule from which a water molecule has been removed (ex. every AA in a protein)
# Monoisotopic mass = computed by using the principal (most abundant) isotope of each atom in the amino acid.
# Average mass = computed by taking the average mass of each atom in the molecule (over all naturally occurring isotopes).
# Many applications in proteomics rely on mass spectrometry. In mass spec, monoisotopic mass is used more often than avg. mass.
# The mass of a protein = sum of the monoisotopic masses of its AA residues + mass of a single water molecule

# Given: A protein string P of length at most 1000 AA.
# Return: The total weight of P.

p = 'CKDKWARKILVGWSIQAWHAAVRKNGDDIQLWCFWRHELNDHWEEVDVAWRQYVYDNYPQKVREMGEDESCITVIYFCMKSQACAPWCMQGRVQGGQEVSSFQSHASQIRYVCDDNEPDPHIYRQDHFLKNNHRPVIPMPYLMPFTALYERKQGFHTQARDNHGDIDYNSSPYQVLEGECKEYNFYSHNVKYGNVPDKYDWRTGCCCMTVKVADLCACFMTNPTNPLGENVPCVDPCERKVVAPFFCDERWPACGLMMWNIMPKVVYMVGMYESMVSCFSLRTRKSTNHGDCFKQNEILKKYGPIFFMQWPVDNIDVTAITPDEASEKMNRTCPFQGEVMRYEVVYYWVWVFPCQDTQVLENFREFPCNDHIITFGWIADRPHHISMKGAGTFRELPGTLATYWHAGESSWWNKDQVMAAFCKDEQKNGHMAAHHWVGMSTGGTEPAECEIMVSMHCHDFHSYSFWVMPTEFIYTWINAFRIVSFFQWYDGWPMKASGQDKAFEGTKIHPSNITDKVGCDGSIAGEEEQGPGCMWMLGSLETNWGTHNLIWWMTGWRAQVPGTENDNHPRTLMFRQQGFCPLLSPSIVSMFFMAEIKTTVDVYELPRNTWWTVELDIVEEPIMRDDNWGKNPADIHTAASFPDVKDFSLFIFHANHMVSGACQDCDKIKCFCHFTSVYEQLVYADSWAPTGPPLPTNWCDLTTDWVKPYSLGNLQNAECSIIYGGVLESCGKHFYEWPEMELHTQCNMMDYLADPDRTFLKPLGHCMRTYQETEDPWGCLWDKNDMFLPWKIFQALKPILGKWMLMWNLHFIHHMHANIKVFRHDDSLWMCNNYTRYAGRGWDDAWCVRHGAIHEGHPKYDFHDTPLEAGHNLTH'

monoisotopic_mass_table = {'A': 71.03711,
                           'C': 103.00919,
                           'D': 115.02694,
                           'E': 129.04259,
                           'F': 147.06841,
                           'G': 57.02146,
                           'H': 137.05891,
                           'I': 113.08406,
                           'K': 128.09496,
                           'L': 113.08406,
                           'M': 131.04049,
                           'N': 114.04293,
                           'P': 97.05276,
                           'Q': 128.05858,
                           'R': 156.10111,
                           'S': 87.03203,
                           'T': 101.04768,
                           'V': 99.06841,
                           'W': 186.07931,
                           'Y': 163.06333,
                           }
h2o = 18.01056
weight = 0
for aa in p:
    weight += monoisotopic_mass_table[aa]

weight
print(weight)
