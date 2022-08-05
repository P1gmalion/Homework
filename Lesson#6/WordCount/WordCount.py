import re

frequency = {}
paper = open('text.txt', 'r')
text = paper.read().lower()
length_capital = re.findall(r'\b[a-z]{3,15}\b', text)

for word in length_capital:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])