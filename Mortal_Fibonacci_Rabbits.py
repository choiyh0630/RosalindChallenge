# Each pair of rabbits reaches maturity in 1 month, and produces a single pair of offspring (1M, 1F) each subsequent month.

# Given: Positive integers n <= 100 and m <= 20
# Return: The total number of pairs of rabbits that will remain after n-th month if all rabbits live for m months.

# F_n = F_n-1 + F_n-2 - F_n-(m+1)

m = 3

def count_rabbits(n):
    rabbits = [0] * (n)
    rabbits[0] = 1
    rabbits[1] = 1
    print(rabbits)
    n -= 1
    for i in range(2, n + 1):
        if i + 1 > m:
            rabbits[i] = rabbits[i - 1] + rabbits[i - 2] - rabbits[i-(m+1)]
        else:
            rabbits[i] = rabbits[i - 1] + rabbits[i - 2]

    return rabbits

print(count_rabbits(6))

k = m
n = 6
f = [0] * (n + 1)
f[0] = 1
for i in range (2, n + 1):
    print(f)
    a =f[i-2]
    b = f[i-1]
    c = f[i-k-1]
    x = i-k-1
    f[i] = f[i-2] + f[i-1] - f[i - k - 1]

print(f[n] + f[n-1])

