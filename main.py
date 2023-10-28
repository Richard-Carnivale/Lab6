# Original contributor: Richard Carnivale


def main():

    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))

    while option != 3:

        while option > 3 or option < 1:
                print("Please enter a valid option")
                option = int(input("Please enter an option: "))

        if option == 3:
            break

        if option == 1:
            try:
                password = input("Please enter your password to encode: ")
                while len(password) != 8:
                    print("Please enter a 8-digit password")
                    password = input("Please enter your password to encode: ")
            except:
                print("There was an error. Try again.")
                password = input("Please enter your password to encode: ")
                while len(password) != 8:
                    print("Please enter a 8-digit password")
                    password = input("Please enter your password to encode: ")

            print("Your password has been encoded and stored!\n")

        try:
            if option == 2:
                encodedPassword = ''

                for i in range(len(password)):
                    encodedPassword += (str((int(password[i]) + 3) % 10))

                print(f"The encoded password is {encodedPassword}, and the original password is {password}.\n")
        except:
            print("Error")
            option = int(input("Please enter an option: "))
            continue

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
