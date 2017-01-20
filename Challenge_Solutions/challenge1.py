import string

"""Python Challenge #1:
   The challenge provides the text that I have set to the variable 'coded_text'
   The clue given eludes that each of the characters should be transformed 2
   alphabetical places forward. As in k->m or O->Q."""


def main():
    coded_text = (
        'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.'
        ' bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm '
        'jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
        )

    # Create list of lowercase alphabet characters
    alphabet = list(string.ascii_lowercase)

    # add characters 'a' and 'b' to end of list. Since I will use this list
    # to decode the 'coded_text' by accessing 2 charcters ahead in list, the
    # case of 'y' and 'z' will create out of index errors.
    alphabet.extend(['a', 'b'])

    decoded = []
    for c in coded_text:
        if c.isalpha():
            pos = alphabet.index(c)
            decoded.append(alphabet[pos + 2])
        else:
            decoded.append(c)

    # Print the decoded message
    print ''.join(decoded)


if __name__ == '__main__':
    main()
