from multipledispatch import dispatch
from bs4 import BeautifulSoup
import requests
import sys

baseurl = "https://tinyurl.com/create.php?source=indexpage&url="


class Shortner:

    @dispatch(str)
    def shorten(self, url):
        source = requests.get(baseurl + url).text
        soup = BeautifulSoup(source, features="html.parser")
        try:
            shortned_link = soup.find("a", {"id": "copy_div"})
            return shortned_link["href"]

        except TypeError:
            print("URL invalid or alias not available")
            exit(1)

    @dispatch(str, str)
    def shorten(self, url, alias):
        source = requests.get(baseurl + url + "&alias=" + alias).text
        soup = BeautifulSoup(source, features="html.parser")
        try:
            shortned_link = soup.find("a", {"id": "copy_div"})
            return shortned_link["href"]

        except TypeError:
            print("URL invalid / Alias not available")
            exit(1)


if __name__ == '__main__':
    try:
        print(Shortner.shorten(sys.argv[1], sys.argv[2]))

    except IndexError:
        try:
            print(Shortner.shorten((sys.argv[1])))
        except IndexError:
            print("Not enough arguments specified... exiting")
            exit(1)
