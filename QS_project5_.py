def add_numbers():
    print("This program adds two numbers. ")

def main():
    stop_loop = "no"
    add_numbers()
    while stop_loop != "bye":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        total = num1 + num2

        print("{} + {} = {}".format(num1, num2, total))
        stop_loop = input("Type 'bye' to exit program: ").lower().strip()


if __name__ == "__main__":
    main()
