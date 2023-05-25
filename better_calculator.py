n1=float(input("Enter number1 "))
op=input("Enter operator") 
n2=float(input("Enter number2 ")) 

if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)  
elif op=="%":
    print(n1%n2)  
else:
    print("Invaild input")