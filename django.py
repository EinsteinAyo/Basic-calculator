
num1=int(input("Enter the first Number: "))
num2=int(input("Enter the second Number: "))
op=input("Enter the operator: ")

if op== '+':
    print("The addition is ",num1+num2)
elif op== '-':
    print("The subtraction is ",num1-num2)
elif op== '*':
    print("The multiplication is ",num1*num2)
elif op=='/':
    print("The division is",num1/num2)
else:
    print("Invalid Operator")