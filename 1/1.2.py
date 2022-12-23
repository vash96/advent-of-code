ans = []
curr = 0
with open("in2", "r") as file:
    for line in file:
        s = line.strip()
        if s == "":
            ans.append(curr)
            curr = 0
        else:
            curr += int(s)
    ans.sort()

print(sum(ans[-3:]))