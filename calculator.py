num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))
mat_op = input("Enter mathematical operator")

if (mat_op == "+"): 
    print(num1, "+", num2, "=", num1 + num2)  # Using commas
elif (mat_op == "-"): 
    print(num1, "-", num2, "=", num1 - num2) 
elif (mat_op == "*"): 
    print(num1, "*", num2, "=", num1 * num2 ) 
elif (mat_op == "/"):
    print(num1, "/", num2, "=", num1 / num2 )
else: 
    print("Enter valid operator") 
