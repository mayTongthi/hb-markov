"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # create a variable called text_string
    # assign open(input_path)
    # read method will be invoke upon the open file
    # return the text_string
    long_string = open(file_path).read()
    return long_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # create a variable = call in the function
        # text_string = open_and_read_file(file_path)
    # split text_string into a list 
        # text_string.split(): I,do,not,like,green,eggs,and,ham
    # loop over the text_string
        # for i in range(len(text_list) -1):
            # chains[(i, i+1)] = i+2
            
    # your code goes here

    text_string = open_and_read_file("green-eggs.txt")
    text_list = text_string.split()
    
    for i in range(len(text_list) - 2):
        text_key = (text_list[i], text_list[i + 1])
        text_value = text_list[i + 2]
        if text_key not in chains:
            # chains[text_key] = []
            chains[text_key] = []

        chains[text_key].append(text_value)
    

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    for word in chains:
        for item in word:
            words.append(item)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

