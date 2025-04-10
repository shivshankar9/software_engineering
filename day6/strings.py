name="shiv"
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())

msg="Hello Python"
print(msg[0:5])
print(msg[-6])
print(msg[:])

print(msg[::2])

#🔹 f-strings (Modern & Recommended)

name="Shiv"
age=23
print(f"My name is {name} and I am {age} years old.")
print("Hello {}, your age is {}".format(name, age))


txt=" pythone is amazing!   "
print(txt)
print(txt.strip())
print(txt.replace("amazing", "powerful"))
print(txt.find("is"))


data="apple, banana,cherry"
print(data)
print(data.strip())
items=data.split(",")
print(items)

joined="-".join(items)
print(joined)