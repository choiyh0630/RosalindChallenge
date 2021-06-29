# Given positive integers n <= 40 and k <= 5,
# return the total number of rabbit pairs that will be present after n months; every pair of reproduction-age rabbits produces a litter of k rabbit pairs

# F_n = # of rabbit pairs alive after n-th month
# Let's dissect the problem down into the fibonacci sequence equations
# F_1 = 1
# F_2 = 1
# F_3 = 4 = F_2 + k*F_1 = 1 + 3(1)
# F_4 = 7 = F_3 + k*F_2 = 4 + 3(1)
# F_5 = 19 = F_4 + k*F_3 = 7 + 3(4)

def count_rabbits(n, k):
    if n == 1 or n == 2:
        total = 1
    else:
        total = count_rabbits(n - 1, k) + k * count_rabbits(n - 2, k)
    return total

print(count_rabbits(29, 2))
