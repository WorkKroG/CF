ff = input()
ff = ff.split()
shovel = int(ff[0])
r = int(ff[1])
k = 1
std = shovel

while (shovel % 10 != 0) & (shovel % 10 != r):
    k += 1
    shovel = std * k

print(k)
