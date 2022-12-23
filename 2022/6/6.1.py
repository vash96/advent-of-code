s = open("in1", "r").read()
for i in range(len(s)):
    ss = set(s[i-4:i])
    print(ss)
    if len(ss) == 4:
        print(i)
        break