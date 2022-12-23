s = open("in2", "r").read()
for i in range(len(s)):
    ss = set(s[i-14:i])
    print(ss)
    if len(ss) == 14:
        print(i)
        break