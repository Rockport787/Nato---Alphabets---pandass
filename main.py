

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas
nato_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:

nato_dict = {row.letter: row.code for (index, row) in nato_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter the name : ").upper()

result = [nato_dict[n] for n in user_name]

print(result)


