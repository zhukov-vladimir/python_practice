k = int(input())
pol = 0
now = 0

if k <= 9:
    pol = k
    now = k
    print(pol)

if 10 <= k <= 99:
    pol = 9
    now = 10
    while now <= k:
        if now // 10 == now % 10:
            pol += 1
        now += 1
    print(pol)

if 100 <= k <= 999:
    pol = 18
    now = 100
    while now <= k:
        if now // 100 == now % 10:
            pol += 1
        now += 1
    print(pol)

if 1000 <= k <= 9999:
    pol = 108
    now = 1000
    while now <= k:
        if now // 100 == (now % 100) // 10 + (now % 10) * 10:
            pol += 1
        now += 1
    print(pol)

if 10000 <= k <= 99999:
    pol = 198
    now = 10000
    while now <= k:
        if now // 1000 == (now % 100) // 10 + (now % 10) * 10:
            pol += 1
        now += 1
    print(pol)
