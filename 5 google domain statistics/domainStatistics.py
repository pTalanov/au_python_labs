__author__ = 'Pavel'

import urllib.parse
import urllib.request
import re

def getHtmlResponseAsString():
    query = input("Query: ")
    query = urllib.parse.urlencode({'q': query})
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    url = 'http://www.google.com/search?' + query
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request).read().decode()
    return response

def parseResultUrlsFromResponse(response):
    target_prefix = '<h3 class="r"><a href="'
    url_re = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    parse_result = re.findall(target_prefix + url_re, response)
    urls = [s[len(target_prefix):] for s in parse_result]
    return urls

def countDomainStatistics(urls):
    dict = {}
    for url in urls:
        domain = urllib.parse.urlparse(url).netloc.split('.')[-1]
        domain_count = dict.get(domain)

        if domain_count is None:
            dict[domain] = 1
        else:
            dict[domain] += 1

    return dict

response = getHtmlResponseAsString()
urls = parseResultUrlsFromResponse(response)
statistics = countDomainStatistics(urls)

print("Domains count:")

for key in statistics:
    print(key + " : " + str(statistics[key]))

