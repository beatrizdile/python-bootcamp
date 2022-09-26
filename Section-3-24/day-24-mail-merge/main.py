PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as other_letter:
            other_letter.write(new_letter)



