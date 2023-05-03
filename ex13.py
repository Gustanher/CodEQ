n = int(input())
alturas = list(map(int, input().split()))

for i in range(1, n):
    if alturas[i] > alturas[i-1] and (i == n-1 or alturas[i+1] < alturas[i]):
        continue
    elif alturas[i] < alturas[i-1] and (i == n-1 or alturas[i+1] > alturas[i]):
        continue
    else:
        print(0)
        break
else:
    print(1)