import json
import difflib

def load_dictionarry(data.jason):

with open("data.json", "r") as file:
    data = json.load(file)

    def get_definition(word, dictionary):
        word_lower = word.lower()
        if word_lower in dictionary:
            return dictionary[word_lower]

            else: close_matches - diff.libget_close_matches(word_lower, dictionary.keys(), n=3)
            if close_matches:
                suggestions = ",".join(close_matches)
                return f"Word not found. Did you mean: {suggestions}?"
                else:
                    return "Word not found in the dictionary."

    #Usage
    dictionary = load_dictionary("dictionary.json")
    word = input("Enter a word:")
    definition = get_definition(word, dictionary)
    print(definition)

    