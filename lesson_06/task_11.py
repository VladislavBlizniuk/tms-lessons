s = [int(el) for el in input().split()]
max_el = s[0]
for el in s:
    if el > max_el:
        max_el = el
print(max_el)