x = int(input(" first Value : "))
y = int(input("Second Value: "))


if x<=0 or y<=0:
    print("invalid value")
    exit()
else:


 def addition(x,y):
   return x+y

def subtraction(x,y):
   return x-y

def multiplication(x,y):
   return x*y

def divide(x,y):
   return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")



if choice == '1':
 print(x, "+", y, "=", add(x, y))

elif choice == '2':
 print(x, "-", y, "=", subtract(x,y))

elif choice == '3':
 print(x, "*", y, "=", multiply(x,y))

elif choice == '4':
 print(x, "/", y, "=", divide(x,y))
else:
 print("Invalid input")