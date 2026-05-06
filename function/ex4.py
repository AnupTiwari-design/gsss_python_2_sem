student = {
    "name": "Anup",
    "age": 22,
    "course": "Python"
}

print(student)

#print(student["name"])



for key in student:
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(key," :",value)