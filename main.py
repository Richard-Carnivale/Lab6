# Original contributor: Richard Carnivale

# encode function made by Richard Carnivale that returns encoded password
def encoded():
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

    encodedPassword = ''

    for i in range(len(password)):
        encodedPassword += (str((int(password[i]) + 3) % 10))
        
    return encodedPassword


def main():

    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))

    while option != 3:

        # input validation
        while option > 3 or option < 1:
                print("Please enter a valid option")
                option = int(input("Please enter an option: "))

        # end main
        if option == 3:
            break


        # encoded function is ran here
        if option == 1:
            encodedPassword = encoded()
            print("Your password has been encoded and stored!\n")

        # need to write and define the decoder function here
        if option == 2:
            pass

        # print menu and ask for option
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
