s={1,2,3}

#s.remove(4)
s.discard(4) # no error if not present
print(s)

#loop in set
s1={1,2,3}
for i in s:
    print(s)
#set operation
a={1,2,3,}
b={2,3,4}
print(a|b)#UNION OF B

print(a&b) #intersection

print(a-b)# difference

print(a ^ b) # Symmetric Difference → {1,4}

l=len(s)
s.clear()
print(a[0])