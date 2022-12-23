ans = 0
with open("in1", "r") as file:
    for line in file:
        n = len(line)
        s1 = set(line[:n//2])
        s2 = set(line[n//2:])
        c = s1.intersection(s2).pop()
        if c.islower():
            ans += ord(c)-ord('a')+1
        else:
            ans += ord(c)-ord('A')+27
print(ans)