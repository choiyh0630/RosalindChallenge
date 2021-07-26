# Each pair of rabbits reaches maturity in 1 month, and produces a single pair of offspring (1M, 1F) each subsequent month.

# Given: Positive integers n <= 100 and m <= 20
# Return: The total number of pairs of rabbits that will remain after n-th month if all rabbits live for m months.

# F_n = F_n-1 + F_n-2 - F_n-(m+1)

m = 3

def count_rabbits(n):
    if n == 1 or n == 2:
        total = 1
    else:
        total = count_rabbits(n - 1) + count_rabbits(n - 2) - count_rabbits(n - (m+1))
    return total

print(count_rabbits(6))
