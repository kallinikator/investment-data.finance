#coding=utf-8

import requests
import re

def get_text(url):
    """ Takes the resulting preview of wikipedia from DuckDuckGo """
    content = requests.get(url)
    text = content.text
    try:
        result = re.search(r"\"AbstractText\":\"(.+?)\"", text).group(1)
        print(len(result))
    except:
        result = "No description found!"
        print(result)
    return result

def parse_companies(company_name):
    """ Creates an valid url for DuckDuckGo """
    name = company_name.replace(" ", "+")
    url = "https://duckduckgo.com/?q={}&t=ffab&ia=web".format(name)
    return url
  
def query_companies(companies):
    """ The main function: Taken an Iterable and returns an  dict of descriptions """
    urls = {}
    for entry in companies:
        urls[entry] = parse_companies(entry)
    result = {}
    for entry, url in urls.items():
        print(entry)
        result[entry] = get_text(url)
    return result

if __name__ == "__main__":
    a = query_companies(["Avalanche Biotechnologies", "Apple Inc.", "Abengoa", "Penis"])
