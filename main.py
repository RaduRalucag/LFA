o = open('date.in', 'r')
t = o.readline().strip()
l = []
for i in range(int(t)):
    l.append(o.readline().strip().split())
p = o.readline().strip()
f = o.readline().strip().split()
with open('cuvinte.in', 'r') as c:
    for cuv in c:
        i = p
        d = [i]
        for lit in cuv:
            for x in range(len(l)):
                if l[x][0] == i and l[x][1] == lit:
                    i = l[x][2]
                    d.append(i)
                    break
        if d[len(d) - 1] in f:
            print("Cuvantul este acceptat:", end=' ')
            for i in range(len(d) - 1):
                print(d[i], "->", end=' ')
            print(d[len(d) - 1])
        else:
            print("Cuvantul nu este acceptat.")
if p in f:
    print("Cuvant vid acceptat:", p)
