def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter operation: ")

    if operator == '+':
        print("The sum is: ", num1 + num2)
    elif operator == '-':
        print("The minus is: ", num1 - num2)
    elif operator == '*':
        print("The multiply is: ", num1 * num2)
    elif operator == '/':
        print("The divide is: ", num1 / num2)
        
while True:
    main()