num1=int(input("enter number: "))
num2=num1//100
num3=num1//10%10
num4=num1%10

if 100<=num1<=999:
    print(num2+num3+num4)
else:
    print("error ")
