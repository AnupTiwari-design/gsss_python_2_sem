lst = [1, 1, 2, 3, 2, 1]

freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

for i in freq:
    if freq.get(i)==1:
        print(i)


r_d=set(lst)
print(r_d)