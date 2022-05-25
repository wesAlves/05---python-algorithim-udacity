def recursive(n):
    if n in {0,1}:
        return n
    return recursive(n-1) + recursive(n-2)

print(recursive(14))