alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    result = ""
    for i in text:
        index_in_alph = alphabet.index(i)
        new_index = index_in_alph + shift
        if new_index <= 25:
            result+=alphabet[new_index]
        else:
            new_index = new_index%26
            result+=alphabet[new_index]
    print(f"The coded text is {result}")


def decrypt(cipher_text, shift_amount):
    result2 = ""
    for i in text:
        index_in_alph = alphabet.index(i)
        new_index = index_in_alph - shift
        result2+=alphabet[new_index]
    print(f"The decoded text is {result2}")


if direction == "encode":
    encrypt(text, shift)

elif direction == "decode":
    decrypt(text, shift)



