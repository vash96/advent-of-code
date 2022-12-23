ans = 0
pts = { 'A' : {'X':4, 'Y':8, 'Z':3},
        'B' : {'X':1, 'Y':5, 'Z':9},
        'C' : {'X':7, 'Y':2, 'Z':6}}

with open("in1", "r") as file:
    for line in file:
        [you, me] = line.strip().split()
        ans += pts[you][me]

print(ans)