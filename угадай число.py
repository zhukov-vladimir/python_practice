n = int(input())
question = ''
answerYES = set()
answerNO = set()
while question != 'HELP':
    question = input()
    if question == 'HELP':
        break
    else:
        answer = input()
    if answer == "YES":
        for now in question.split():
            answerYES.add(now)
    else:
        for now in question.split():
            answerNO.add(now)
print(*sorted(list(answerYES - (answerYES & answerNO))))