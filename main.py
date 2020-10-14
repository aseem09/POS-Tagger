from reader import parse_data, list_to_freq_dict, parse_data_get_attrib
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import pprint
import os
import json

pp = pprint.PrettyPrinter(indent=4)
path = 'Train-corpus/'

word_list = []
tag_list = []
word_tags_list = []

for subdir, dirs, files in os.walk(path):
    for file in files:

        fileName = subdir + '/' + str(file)
        words, tags, word_tags = parse_data(fileName)

        word_list.extend(words)
        tag_list.extend(tags)
        word_tags_list.extend(word_tags)


word_dict = list_to_freq_dict(word_list)

with open('words.json', 'w') as outfile:
    json.dump(word_dict, outfile, indent=4)

k1 = Counter(word_dict)
top_words = k1.most_common(10)
print('Top 10 Words are: ')
for i in top_words:
    print(i[0], " :", i[1], " ")

top_words = k1.most_common(25)
keys, values = [i[0] for i in top_words], [i[1] for i in top_words]
plt.pie(values, labels=keys)
plt.show()

print('\n\n')

tag_dict = list_to_freq_dict(tag_list)
with open('tags.json', 'w') as outfile:
    json.dump(tag_dict, outfile, indent=4)

k1 = Counter(tag_dict)
top_tags = k1.most_common(10)
print('Top 10 Tags are: ')
for i in top_tags:
    print(i[0], " :", i[1], " ")

top_tags = k1.most_common(25)
keys, values = [i[0] for i in top_tags], [i[1] for i in top_tags]
plt.pie(values, labels=keys)
plt.show()

print('\n\n')

word_tags_dict = list_to_freq_dict(word_tags_list)
with open('word_tags.json', 'w') as outfile:
    json.dump(word_tags_dict, outfile, indent=4)
