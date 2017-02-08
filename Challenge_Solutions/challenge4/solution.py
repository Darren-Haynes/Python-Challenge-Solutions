"""
   I found this challenge a bit tricky. You download a page run from a php
   script. That page gives you numbers that you use to replace the numbers
   at the end of the present url with the new numbers. Repitition begins, so
   I figured recursion would be appropriate. However, there are a few pages
   that dish up 2 sets of numbers and the later set is the required ones.
   Eventually you hit a page that contain the html suffix for the url which
   is the solution that gets you to the next puzzle in this challenge. You
   have to account for this page when it comes, otherwise you me recursive
   for all eternity. There are a few other traps too, they will be in the
   function comments
"""

import urllib2

BEGIN = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"


def get_digits_from_web_page(url, suffix):
    """Download content from each url and get the digits in that content
       and return them for contructing the next url to check"""

    web_page = urllib2.urlopen(url).read()
    digits = ''.join(char for char in web_page if char.isdigit())
    non_digits = ''.join(char for char in web_page if not char.isdigit())

    # 'html' means we have found what we need
    if 'html' in non_digits:
        return non_digits
    # Accounts for the tricky (and rare) case when a number is not supplied
    # but a message to divide presents number by 2
    elif digits is '':
        digits = int(suffix) / 2
        return str(digits)
    # In a few tricky instances 2 sets of numbers are giving. The message
    # states that the second set of numbers are the ones needed. Since the
    # first set of numbers are always 5 digits long they are cut out using
    # string slicing
    elif len(digits) > 5:
        return digits[5:]
    else:
        return digits


def get_new_url(url, suffix):
    """Recursive function that keeps generating the new url to scrape until
       we find the page we are looking for"""

    digits = get_digits_from_web_page(url, suffix)
    # if 'html' string exists we have found what we need
    if 'html' in digits:
        return digits

    new_url = url.replace(suffix, digits)
    return get_new_url(new_url, digits)


def main():
    """Start process by feeding the first url (in variable "BEGIN") and its
    number id "12345" to function "get_new_url()" which is found at the end
    of the url and each new generated url"""

    suffix = get_new_url(BEGIN, '12345')
    prefix = "http://www.pythonchallenge.com/pc/def/"
    solution = prefix + suffix
    # this prints the url that solves this challenge
    print solution


if __name__ == '__main__':
    main()
