import xml.etree.ElementTree as ET

# XML file to list
def parse_data(file):

    # generate element tree from the XML file
    tree = ET.parse(file)

    # get access to the tree root
    root = tree.getroot()

    # create empty list to store 'word_tag'
    word_tags = []

    # get all <w> tags in the XML file
    for word in root.iter('w'):

        # 'hw' attrib contains the word and 'c5' attrib contains the tag
        word_tag = word.attrib['hw'] + '_' + word.attrib['c5']

        # add element to list
        word_tags.append(word_tag)

    return word_tags


# convert list to dictionary with frequencies
def list_to_freq_dict(word_tags_list):

    # create empty dict
    word_tags_dict_freq = {}

    for i in word_tags_list:

        freq = word_tags_dict_freq.get(i)

        # initialize freq with count 1
        if freq is None:
            word_tags_dict_freq[i] = 1

        # if present increment by 1
        else:
            freq = freq + 1
            word_tags_dict_freq[i] = freq

    return word_tags_dict_freq


