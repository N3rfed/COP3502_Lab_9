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