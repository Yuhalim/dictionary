import json
from difflib import get_close_matches

data = json.load(open('data.json'))
word = input('what word do you want to search: ')


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        question = input('did you mean to type {} instead?. If yes press Y and if no press N: '.format(get_close_matches(word, data.keys())[0]))
        if question == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif question == 'n':
            return 'this word is not in the dictionary, sorry, please type in another word'
    else:
        return 'this word is not in this dictionary'


output = (search(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)