mylist = list(map(int, input().split()))
height = int(input())
index = 0
for i in range(len(mylist)):
    if mylist[i] >= height:
        index = i
print(index + 2)
