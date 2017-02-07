"""
   Regex is needed to get the answer to unlock the next url. The clue is
   "One small letter, surrounded by EXACTLY three big bodyguards on each of
   its sides". So we are looking for a lowercase letter with 3 capital
   letters either side of it (but not 4 or more either side).
"""

import re
import urllib2

URL = "http://www.pythonchallenge.com/pc/def/equality.html"


def get_url():
    """Open url and read source page"""

    return urllib2.urlopen(URL).read()


def solution():
    """Return all matching regex patterns as a list. Join list to reveal
       solution"""

    pattern = r'[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]'
    result = re.findall(pattern, get_url())
    answer = ''.join(result)
    print answer
    

def main():
    solution()


if __name__ == '__main__':
    main()
