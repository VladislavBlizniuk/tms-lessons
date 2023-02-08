s = list(input().split())
new_s = []
for el in s:
    intel = int(el)
    new_s.append(intel)

print(new_s)

summa = 0
for el in new_s:
    summa += el
print(summa)



