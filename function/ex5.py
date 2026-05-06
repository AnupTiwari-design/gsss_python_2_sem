list=[]

print('enter a no')
for i in range(5):
    list.append(int(input()))

even=0
odd=0
for i in list:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1

print(odd)
print(even)