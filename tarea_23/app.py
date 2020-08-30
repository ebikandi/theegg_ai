from solitaire import encrypt, decrypt

if __name__ == '__main__':
    msg = str(input("Write down message to encrypt\n"))
    [encoded, cards] = encrypt(msg)
    print("Encoded message: ", encoded)
    decoded = decrypt(encoded, cards)
    print("Decoded message:", decoded)