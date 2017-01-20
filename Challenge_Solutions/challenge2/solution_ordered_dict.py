"""Python Challenge #2
   Find rare characters in a mass of characters found in the page source of
   this challenge"""

from collections import OrderedDict
from data import data_mess


def main():
    """Use ordered dict to store frequency of characters found in 'data_mess'.
       Those with frequency of just 1 show the message"""

    # Ordered dict used to key order of low frequency characters found
    frequency = OrderedDict()

    for char in data_mess:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Extract message from dict into a string
    message = ''
    for key in frequency:
        if frequency[key] == 1:
            message += key

    print message


if __name__ == '__main__':
    main()
