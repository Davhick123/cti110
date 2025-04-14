def main():
    run_again = "yes"

    while run_again.lower() == "yes":
        user_input = int(input("Enter an integer: "))

        if user_input >= 0:
            for i in range(1, 13):
                print(f"{user_input} * {i} = {user_input * i}")
        else:
            print("This program does not handle negative numbers.")

        run_again = input("\nWould you like to run the program again? ")

    print("\nExiting program...")

main()