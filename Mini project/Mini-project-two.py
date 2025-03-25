# 2. **Simple Calculator** (Addition, Subtraction, etc.)  
# A program : It will ask for input and what arithmetic operation they want to do.Then the program will do it for them

print("Simple calculator! Please write down which arithmetic operation you want to do! +,-,*,/")
operator_input = input("What arithmetic operation you want to do! +,-,*,/ :  ")
c = "+"
d = "-"
e = "*"
f = "/"
if operator_input == c:
    cx = float(input("Please enter your first number : ") )
    kx = float(input("Please enter your second number : ") )
    print(f"The result :{cx+kx}")
elif operator_input == d:
    cx = float(input("Please enter your first number : ") )
    kx = float(input("Please enter your second number : ") )
    print(f"The result :{cx-kx}")
elif operator_input == e:
    cx = float(input("Please enter your first number : ") )
    kx = float(input("Please enter your second number : ") )
    print(f"The result :{cx*kx}")
elif operator_input == f:
    cx = float(input("Please enter your first number : ") )
    kx = float(input("Please enter your second number : ") )
    print(f"The result :{cx/kx}")
else:
    print("Invalid operator Given")
    