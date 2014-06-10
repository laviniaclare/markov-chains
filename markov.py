#!/usr/bin/env python

""" 1. get a random key from the chain_dict using random.sample(chain_dict, 1)
2. get random number method to generate random number for starting point in the value 
    list associated with a tuple.
3. initialize empty list (use .join() at the end to make it a string)
END. Get program to accept input file from command line.
"""

import sys
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
    starting_key = random.sample(chain_dict, 1)

    while len(output) < 10 or output[-1][-1] != ".":
        # append starting key to list
        starting_key = starting_key[0]
        output.append(starting_key[0])
        output.append(starting_key[1])
        # next, append random element of key's value to the output list.
        next_word_index = random.randint(0, len(chain_dict[starting_key]) - 1)
        next_word = chain_dict[starting_key][next_word_index]
        output.append(next_word)

        starting_key = [(starting_key[1], next_word)]

    return " ".join(output)

def main():
    #args = sys.argv

    # Change this to read input_text from a file
    input_text = open("twain.txt")
    read_text = input_text.read()
    corpus = read_text.split()

    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
