# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

with open("nato_phonetic_alphabet.csv") as nato_file:
    to_organize_dict = nato_file
    to_organize_dict = pandas.read_csv(to_organize_dict)

# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in to_organize_dict.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Insert word: ").upper()
user_list = [nato_dict[letter] for letter in user_word]
print(user_list)
