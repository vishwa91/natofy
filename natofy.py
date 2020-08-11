#!/usr/bin/env python

'''
    Simple script to convert a name (or word) to NATO alphabets
'''

# System imports
import os
import sys

NATO_DICT = {'A': 'Alpha',
             'B': 'Bravo',
             'C': 'Charlie',
             'D': 'Delta',
             'E': 'Echo',
             'F': 'Foxtrot',
             'G': 'Golf',
             'H': 'Hotel',
             'I': 'India',
             'J': 'Juliett',
             'K': 'Kilo',
             'L': 'Lima',
             'M': 'Mike',
             'N': 'November',
             'O': 'Oscar',
             'P': 'Papa',
             'Q': 'Quebec',
             'R': 'Romeo',
             'S': 'Sierra',
             'T': 'Tango',
             'U': 'Uniform',
             'V': 'Victor',
             'W': 'Whiskey',
             'X': 'Xray',
             'Y': 'Yankee',
             'Z': 'Zulu',
             ' ': '-'}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Prints NATO words for individual letters in a set of words')
        print('')
        print('Usage:')
        print('\tnatofy word1 word2 ... wordN')
        print('Example:')
        print('\tnatofy Tom Sawyer')
        print('\tTango Oscar Mike Sierra - Alpha Whiskey Yankee Echo Romeo')
        sys.exit()

    word = sys.argv[1]
    for idx in range(2, len(sys.argv)):
        word += ' '
        word += sys.argv[idx]

    nato_letters = [NATO_DICT[letter.upper()] for letter in word]

    print('\n', end='')
    for nato_letter in nato_letters:
        print('%s '%nato_letter, end='')

    print('\n')
