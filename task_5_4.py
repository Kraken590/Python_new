'''a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end=' ')'''

sdr = [500, 10, 9, 34, 56, 1, 5, 100, 700, 1, 780, 1230, 5500]
result = [sdr[i] for i in range(1, len(sdr)) if sdr[i] > sdr[i - 1]]
print(result)