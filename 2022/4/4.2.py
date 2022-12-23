ans = 0
with open("in2", "r") as file:
    for line in file:
        s1,s2 = line.split(',')
        a,b = s1.split('-')
        c,d = s2.split('-')
        [a,b,c,d] = map(int, [a,b,c,d])
        ans += (a <= c <= b) or (c <= a <= d)
print(ans)