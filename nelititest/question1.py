import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation


def word_frequencies(url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """

    # using the request make a get request to the url
    r = requests.get(url)

    # using get the content of the html page
    soup = BeautifulSoup(r.content)

    # join all the text in all the tags
    text = (''.join(s.findAll(text=True))for s in soup.findAll())

    # use counter to count all the instances of words in the text
    c = Counter((x.rstrip(punctuation).lower()
                for y in text for x in y.split()))
    print(c)
