s = input()
first = s.find('h')
last = s.rfind('h')
s1 = s.replace('h', 'H')
print(s1[:first] + 'h' + s1[first + 1:last] + 'h' + s1[last + 1:])
