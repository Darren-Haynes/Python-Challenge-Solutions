"""
   So the source page clearly shows that you need to download and open a pickle
   file linded to on that page. Opening the file will present a list of lists.
   And each inner list contains tuples. The first index of each tuple is either
   a " " or a "#". The second index is a number between 1-95. This first led
   me up the garden path thinking that I may need to convert these numbers to
   unicode or ascii, yet that doesn't account for what the first index of
   either a space of a hash symbol is needed for. It eventually occured to me
   that it may just print out a message to the screen, which is the case!
   """

import pickle
import urllib2

PICKLE_URL = "http://www.pythonchallenge.com/pc/def/banner.p"


def main():
    """Download and open pickle file. Pickle file is list of lists. Loop
       through lists and print the first index of the tuple pairs times the
       intger provided by the second index. The solution will be printed"""
    info = urllib2.urlopen(PICKLE_URL)
    p = pickle.load(info)
    for lst in p:
        print ''.join(char * num for char, num in lst)


if __name__ == '__main__':
        main()
