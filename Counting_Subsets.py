n = 973

def b(n):
    if n == 0:
        return 1
    return 2*b(n-1) % 10**6

print(f'The total number of subsets of a set with {n} elements: {b(n)}')
