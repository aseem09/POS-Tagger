from reader import parse_data, list_to_freq_dict
import pprint

pp = pprint.PrettyPrinter(indent=4)

word_tags_list = parse_data('Train-corpus/A1/A1B.xml');

word_tags_dict = list_to_freq_dict(word_tags_list)

pp.pprint(word_tags_dict)
