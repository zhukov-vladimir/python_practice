inFile = open('input.txt', 'r', encoding='utf8')
k = int(input())
s = []
s_sum = []
for line in inFile:
    p = line.split()
    threeExam = int(p[-1])
    twoExam = int(p[-2])
    oneExam = int(p[-3])
    if (threeExam >= 40) and (twoExam >= 40) and (oneExam >= 40):
        s.append((threeExam, twoExam, oneExam))
        s_sum.append(threeExam + twoExam + oneExam)
s_sum.sort(reverse=True)
tabl = []
n = 0
while n < len(s_sum):
    tabl.append((s_sum[n], s_sum.count(s_sum[n])))
    n += s_sum.count(s_sum[n])
count = 0
ball = s_sum[0]
if len(s_sum) > k:
    print('0')
elif s_sum.count(max(s_sum)) > k:
    print('1')
else:
    for i in tabl:
        if (count + i[1]) <= k:
            count += i[1]
            ball = i[0]
        else:
            break
    print(ball)
