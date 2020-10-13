import xml.etree.ElementTree as ET

# XML file to list


def parse_data(file):

    # generate element tree from the XML file
    tree = ET.parse(file)

    # get access to the tree root
    root = tree.getroot()

    # create empty list to store 'word_tag'
    word_tags = []

    # create empty list to store 'word'
    words = []

    # create empty list to store 'tag'
    tags = []

    # get all <w> tags in the XML file
    for w_tag in root.iter('w'):

        # 'hw' attrib contains the word and 'c5' attrib contains the tag
        word = w_tag.attrib['hw']
        tag = w_tag.attrib['c5']

        word_tag = word + '_' + tag

        # adding the word to the words list
        words.append(word)

        # adding the tag to the tags list
        tags.append(tag)

        # add element to list
        word_tags.append(word_tag)

    return (words, tags, word_tags)

# XML file to list


def parse_data_get_attrib(file, attrib):

    # generate element tree from the XML file
    tree = ET.parse(file)

    # get access to the tree root
    root = tree.getroot()

    # create empty list to store 'word_tag'
    word_attribs = []

    # get all <w> tags in the XML file
    for word in root.iter('w'):

        # 'hw' attrib contains the word and 'c5' attrib contains the tag
        word_attrib = word.attrib[attrib]

        # add element to list
        word_attribs.append(word_attrib)

    return word_attribs

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
