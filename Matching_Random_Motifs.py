# Promoter = regions of DNA that initiate the transcription of a gene. It's usually located shortly before the start of its gene,
#            and it contains specific intervals of DNA that provide an initial binding site for RNA polymerase to initiate transcription.
#            Finding a promoter is usually the second step in gene prediction after establishing the presence of an ORF (Open Reading Frame).
# There's no quick rule for identifying promoters as they vary by species (additional intervals used to bind to specific proteins
# or to change the intensity of transcription). Most eukaryotic promoters are harder to characterize; they have a TATA box, preceded by an interval
# called a B recognition element (BRE), typically located within 40 bp of the start of transcription, and can hold additional "regulatory" intervals.

# Aim in this problem is to determine the probability with which a given motif (ex. promoter) occurs in a randomly constructed genome.
# For any event = P(A) + P(A_c) = 1

# Given: A positive integer N <= 100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
# Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x, then
#         at least one of the strings equals s. Same random string can be created more than once.

N = 90000
x = 0.6
s = 'ATAGCCGA'

def prob_s(s, x):
    p = 1
    p_gc = x/2
    p_at = (1 - x)/2
    for i in s:
        if i == 'A' or i == 'T':
            p *= p_at
        else:
            p *= p_gc
    return p

print(prob_s(s, x))

def no_prob_s(s, x, N):
    p = 1
    p_g = p_c = x/2
    p_a = p_t = (1 - x)/2
    for n in s:
        if n == 'A':
            p *= 1 - p_a
        elif n == 'T':
            p *= 1 - p_t
        elif n == 'G':
            p *= 1 - p_g
        else:
            p *= 1 - p_c
    return 1 - p ** N

print(no_prob_s(s,x,N))
