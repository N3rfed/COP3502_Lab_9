def encoder(password):
    encoder = ""
    encoder += str(password)
    encoded_password = ""
    for i in range(len(encoder)):
        increment = int(encoder[i])
        increment += 3
        if increment > 9:
            encoded_password += str(increment)[-1]
            continue
        encoded_password += str(increment)
    return encoded_password


def decoder(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        if int(digit) > 2:
            decoded_password += str(int(digit) - 3)
        elif int(digit) < 3:
            decoded_password += str(int(digit) + 7)
    return decoded_password


def main():
    encoded_password = ""
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        user_choice = input("Please enter an option: ")
        if user_choice == "1":
            encode = input("Please enter your password to encode: ")
            encoded_password = encoder(encode)
            print("Your password has been encoded and stored!\n")
        elif user_choice == "2":
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif user_choice == "3":
            quit()
if __name__ == "__main__":
    main()