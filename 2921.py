n = int(input())
total = 0
for i in range(n+1):
    for j in range(i+1):
        total += i
        total += j
print(total)
