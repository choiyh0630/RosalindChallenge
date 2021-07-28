# Each pair of rabbits reaches maturity in 1 month, and produces a single pair of offspring (1M, 1F) each subsequent month.

# Given: Positive integers n <= 100 and m <= 20
# Return: The total number of pairs of rabbits that will remain after n-th month if all rabbits live for m months.

# F_n = F_n-1 + F_n-2 - F_n-(m+1)

k = 17
n = 81
f = [0] * (n + 1)
f[0] = 1
for i in range (2, n + 1):
    f[i] = f[i-2] + f[i-1] - f[i - k - 1]

print(f[n] + f[n-1])

