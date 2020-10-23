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
        word = w_tag.text.replace(" ", "")
        tag = w_tag.attrib['c5']

        words.append(word)

        if '-' in tag:
            tag1 = tag[:3]
            tag2 = tag[4:]
            word_tag1 = word + '_' + tag1
            word_tag2 = word + '_' + tag2

            tags.append(tag1)
            word_tags.append(word_tag1)
            tags.append(tag2)
            word_tags.append(word_tag2)

        else:
            word_tag = word + '_' + tag
            tags.append(tag)
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
