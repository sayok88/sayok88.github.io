import json

words = []
with open('dictionary.json') as json_file:
    data = json.load(json_file)
    words = list(data.keys())

with open("words.json", "w") as outfile:
    json.dump(words, outfile)

words_5 = list(filter(lambda x: len(x)==5, words))

with open("five_letter_words.json", "w") as outfile:
    json.dump(words_5, outfile)
