fin = open('input2.txt')
myDict = {}
for word in fin.read().split():
    myDict[word] = myDict.get(word, 0) + 1
wordList = sorted(myDict.items())
wordList.sort(key=lambda s: s[1], reverse=True)
print(wordList[0][0])
