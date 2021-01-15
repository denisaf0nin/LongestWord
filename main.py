# What are the longest words that can be typed using only letters from the top row of a keyboard?

from nltk.corpus import words
word_list = words.words()

# Function return 10 longest English words consisting only of letter in a string 'row':
def getWords(row):
    letters = set([x for x in row])

    results = []

    for word in word_list:
        word_letters = set([x for x in word.lower()])
        n = 0
        for letter in word_letters:
            if letter in letters:
                n += 1
            else:
                break
        if n == len(word_letters):
            results.append(word)

    sorted_results = sorted(results, key=len, reverse=True)

    for i in range(10):
        print(f'{i+1}. {sorted_results[i]} - {len(sorted_results[i])} letters')

top_row = 'qwertyuiop'
getWords(top_row)
