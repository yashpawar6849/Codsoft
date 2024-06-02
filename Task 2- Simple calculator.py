print("Welcome to TotalEase-your handy tool for quick calculations")

while True:
    print("1=Addition")
    print("2=Substraction")
    print("3=Multiplication")
    print("4=Division")

    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))

    if choice == "1":
        print(num1,"+",num2,"=",(num1+num2))
    elif choice =="2":
        print(num1,"-",num2,"=",(num1-num2))
    elif choice =="3":
        print(num1,"*",num2,"=",(num1*num2))
    elif choice =="4":
        print(num1,"/",num2,"=",(num1/num2))

    print("Enter Quit or Exit")

    choice=input("Enter your choice here:") 
    if choice == "Quit" or choice == "Exit":
        break