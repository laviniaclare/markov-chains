#!/usr/bin/env python

"""
To do: deal with quotation marks.
END. Get program to accept input file from command line.
"""

from sys import argv
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chain_dict = {}

    for i in range(len(corpus) - 2):
        if not chain_dict.get((corpus[i], corpus[i + 1])):
            chain_dict[(corpus[i], corpus[i + 1])] = [corpus[i + 2]]
        else:
            chain_dict[(corpus[i], corpus[i + 1])].append(corpus[i + 2])

    return chain_dict

def make_text(chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    output = []

    # generate random starting key and assign both elements to empty list
    starting_key = random.sample(chain_dict, 1)
    output.append(starting_key[0][0])
    output.append(starting_key[0][1])

    # initialize next_key to be starting_key for first pass thru loop
    next_key = starting_key
    sentence_ends=['.','!','?']

    # go thru loop until length of output >= 10 or element of 
    # sentence_ends is encountered.
    while len(output) < 10 or output[-1][-1] not in sentence_ends:
        # convert tuple-inside-list back to tuple
        next_key = next_key[0]

        # next, append random element of key's value to the output list.
        next_word_index = random.randint(0, len(chain_dict[next_key]) - 1)
        next_word = chain_dict[next_key][next_word_index]
        output.append(next_word)

        # define next key as second element of previous key, and next_word
        next_key = [(next_key[1], next_word)]

    return " ".join(output)

def main():

    script, filename = argv

    # Change this to read input_text from a file
    input_text = open(filename)
    read_text = input_text.read()
    corpus = read_text.split()

    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
