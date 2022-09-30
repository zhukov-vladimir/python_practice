x = int(input())


def mindiv(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1


print(mindiv(x))
