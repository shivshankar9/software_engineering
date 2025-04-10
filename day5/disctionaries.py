#Dictionaries – Key-Value Pairs
student={
    "name":"shiv",
    "age" : 22,
    "course":"python"

}
print(student)
student["age"]=23
print(student)

for key, value in student.items():
    print(key, ":",value)