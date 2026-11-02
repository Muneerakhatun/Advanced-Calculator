while True:
    print("\n"+ "=" * 40)
    print("          ADVANCED CALCULATOR")
    print("=" * 40)
    print("\n Choose an operation:")
    print("_" *40,"\n")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Exit")

    print("_" * 40,)
    print()

    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number from 1 to 8.")
        continue
    if choice==8:
            print("Thank You for using the calculator!")
            break
    if choice<1 or choice>8:
        print("Invalid choice! Please select between 1 to 8.")

    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice==1:
        print("Result:",num1+num2)
    elif choice==2:
        print("Result:",num1-num2)
    elif choice==3:
        print("Result:",num1*num2)
    elif choice==4:
        if num2==0:
            print("Error! Cannot divide by zero.")
        else:
            print("Result:",num1/num2)
    elif choice==5:
        print("Result:",num1%num2)
    elif choice==6:
        print("Result:",num1**num2)
    elif choice==7:
        if num1<0:
            print("Error! Cannot calculate square root of a negative number.")
        else:
            print("Result:",num1**0.5) #power= root or ^1/2 or ^0.5
    else:
        print("Invalid choice!")
