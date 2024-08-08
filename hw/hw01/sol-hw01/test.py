def largest_factor(n):
    factor = n-1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1
    return 1

num=15
result = largest_factor(num)
print(result)
