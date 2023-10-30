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

def decode_password(password): # This decode function was made by Emir Erkilic that returns the decoded password, and is used when option 2 is selected.
    decoded = ""
    for char in str(password):
        if char.isdigit():
            digit = int(char)
            if 3 <= digit <= 9:
                decoded_digit = (digit - 3) % 10
            else:
                decoded_digit = (digit + 7) % 10
            decoded += str(decoded_digit)
        else:
            decoded += char
    return decoded

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

        # This section of the code "if option == 2:" was written by Emir Erkilic, and it implements the decode_password function.
        if option == 2:
            if encodedPassword is not None:
                decoded_password = decode_password(encodedPassword)
                print(f"The encoded password is {encodedPassword}, and the original password is {decoded_password}.\n")
            else:
                print("No password has been encoded yet.")

        # print menu and ask for option
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
