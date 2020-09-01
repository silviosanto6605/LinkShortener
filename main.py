from multipledispatch import dispatch
from bs4 import BeautifulSoup
import requests

baseurl = "https://tinyurl.com/create.php?source=indexpage&url="



class Shortner:
    
    try:
        def __init__(self, url, alias):
            self.url = ""
            self.alias = ""
    
        @dispatch(str, str)
        def shorten(self, url, alias):
            source = requests.get(baseurl + url+"&alias="+alias).text
            soup = BeautifulSoup(source, features="html.parser")
            shortned_link = soup.find("a",{"id":"copy_div"})
            return shortned_link["href"]
    
    
        @dispatch(str)
        def shorten(self, url):
            source = requests.get(baseurl + url).text
            soup = BeautifulSoup(source, features="html.parser")
            shortned_link = soup.find("a",{"id":"copy_div"})
            return shortned_link['href']
        
    except TypeError:
        print("Alias not available")


