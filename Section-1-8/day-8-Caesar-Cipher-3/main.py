import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def ceasar(text, shift, direction):
    result = ""
    if direction == "encode":
        for i in text:
            if i not in alphabet:
                result += i
                continue
            index_in_alph = alphabet.index(i)
            new_index = index_in_alph + shift
            if new_index <= 25:
                result+=alphabet[new_index]
            else:
                new_index = new_index%26
                result+=alphabet[new_index]
        print(f"The coded text is: {result}")

    elif direction == "decode":
        for i in text:
            if i not in alphabet:
                result += i
                continue
            index_in_alph = alphabet.index(i)
            new_index = index_in_alph - shift
            result+=alphabet[new_index]
        print(f"The decoded text is: {result}")

game = True

while game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)
    if input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n") == "no":
        print("Goodbye")
        game = False
    

