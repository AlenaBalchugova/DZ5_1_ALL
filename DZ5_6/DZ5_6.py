L = {}
D = list()
with open('Text111.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
for line1 in lines:
    D = line1.replace('(', ' ').split()
    print(D[0][:-1])
    L[D[0][:-1]] = sum(
                int(i) for i in D if i.isdigit()
            )
print(L)