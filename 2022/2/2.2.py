ans = 0
pts = { 'A' : {'X':3, 'Y':4, 'Z':8},
        'B' : {'X':1, 'Y':5, 'Z':9},
        'C' : {'X':2, 'Y':6, 'Z':7}}

with open("in2", "r") as file:
    for line in file:
        [you, me] = line.strip().split()
        ans += pts[you][me]

print(ans)