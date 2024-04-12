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
def decoder(password):
    decoder = ""
    decoder += str(password)
    decoded_password = ""
    for i in range(len(decoder)):
        decrement = int(decoder[i])
        decrement -= 3
        if decrement < 0:
            decoded_password += str(decrement)[-1]
            continue
        decoded_password += str(decrement)
    return decoded_password

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        user_choice = input("Please enter an option:")
        if user_choice == "1":
            encode = input("Please enter your password to encode:")
            passcode = encoder(encode)
            print("Your password has been encoded and stored!\n")
        elif user_choice == "2":
           decoded_passcode = decoder(passcode)
           print("The encoded password is ", passcode, "and the original password is ", decoded_passcode)
        elif user_choice == "3":
            quit()
if __name__ == "__main__":
    main()