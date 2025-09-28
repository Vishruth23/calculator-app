from calculator import sqrt, power, factorial, log

def menu():
    print("\nSelect operation:")
    print("1. Square Root")
    print("2. Power")
    print("3. Factorial")
    print("4. Logarithm")
    print("5. Exit")

def main():
    while(True):
        menu()
        choice = input("Enter choice(1/2/3/4/5): ")

        try:
            if choice == '1':
                num = float(input("Enter number: "))
                print(f"Square Root of {num} is {sqrt(num)}")
            elif choice == '2':
                base = float(input("Enter base: "))
                exp = float(input("Enter exponent: "))
                print(f"{base} raised to the power of {exp} is {power(base, exp)}")
            elif choice == '3':
                num = int(input("Enter number: "))
                print(f"Factorial of {num} is {factorial(num)}")
            elif choice == '4':
                num = float(input("Enter number: "))
                print(f"Natural Logarithm of {num} is {log(num)}")
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid Input, try again.")
        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()

