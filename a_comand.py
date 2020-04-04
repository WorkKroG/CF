n = input()
k = 0
for i in range(0, int(n)):
    mn = input()
    if mn.count('1') >= 2:
        k += 1
print(k)
