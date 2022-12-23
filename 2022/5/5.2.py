conf = [[], "N V C S".split(), "S N H J M Z".split(), "D N J G T C M".split(), "M R W J F D T".split(), "H F P".split(), "J H Z T C".split(), "Z L S F Q R P D".split(), "W P F D H L S C".split(), "Z G N F P M S D".split()]

def Move(n, f, t):
    conf[t] = conf[f][:n] + conf[t]
    conf[f] = conf[f][n:]

with open("in2", "r") as file:
    for line in file:
        n, f, t = map(int, line.replace('move ', '').replace('from ', '').replace('to ', '').split())
        Move(n, f, t)

print(''.join([conf[i][0] for i in range(1, len(conf))]))