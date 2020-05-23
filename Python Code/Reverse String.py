def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s =input("enter name:")
print("The reversed name is : ",reverse(s))

