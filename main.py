from reader import parse_data, list_to_freq_dict, parse_data_get_attrib
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=4)
fileName = 'Train-corpus/A1/A1B.xml'

word_list = parse_data_get_attrib(fileName, 'hw')
word_dict = list_to_freq_dict(word_list)
k1 = Counter(word_dict)
top_words = k1.most_common(10)
print('Top 10 Words are: ')
for i in top_words:
    print(i[0]," :",i[1]," ")

top_words = k1.most_common(25)
keys, values = [i[0] for i in top_words],[i[1] for i in top_words]
plt.pie(values, labels=keys)
plt.show()

print('\n\n')

tag_list = parse_data_get_attrib(fileName, 'c5')
tag_dict = list_to_freq_dict(tag_list)
k1 = Counter(tag_dict)
top_tags = k1.most_common(10)
print('Top 10 Tags are: ')
for i in top_tags:
    print(i[0]," :",i[1]," ")

top_tags = k1.most_common(25)
keys, values = [i[0] for i in top_tags],[i[1] for i in top_tags]
plt.pie(values, labels=keys)
plt.show()

print('\n\n')

word_tags_list = parse_data(fileName)
word_tags_dict = list_to_freq_dict(word_tags_list)

# pp.pprint(word_list)
