ans = 0
curr = 0
with open("in1", "r") as file:
    for line in file:
        s = line.strip()
        if s == "":
            curr = 0
        else:
            curr += int(s)
        ans = max(ans, curr)

print(ans)