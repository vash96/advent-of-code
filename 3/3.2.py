ans = 0
file = open("in2", "r")
lines = [s.strip() for s in file.readlines()]
groups = [lines[3*i:3*i+3] for i in range(len(lines)//3)]
for g in groups:
    [s1, s2, s3] = list(map(set, g))
    c = s1.intersection(s2.intersection(s3)).pop()

    if c.islower():
        ans += ord(c)-ord('a')+1
    else:
        ans += ord(c)-ord('A')+27
print(ans)