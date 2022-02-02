import json
letters = input()
letters  = set([l for l in letters])
print(letters)

words = []
with open('five_letter_words.json') as json_file:
    data = json.load(json_file)
cnt = len(letters)
for word in data:
    flag = 0
    for l in letters:
        if l in word:
            flag+=1
    if flag == cnt:
        words.append(word)


for x in words:
    print(x)
