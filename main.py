import pandas

nato = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dictionary = {row.letter: row.code for (index, row) in nato.iterrows()}

name = input("Please type your name: ")
result = [nato_dictionary.get(n.upper()) for n in name]

print(result)

