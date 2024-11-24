k = int(input())

ans = []

for a in range(1, 21):
    for b in range(1, 21):
        if a == b or (a, b) in ans:
            continue

        if k % (a + b) == 0:
            ans.append((b, a))

for x in ans:
    print(x[1], x[0], sep='', end='')
print()
