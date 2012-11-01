__author__ = 'Pavel'

import urllib.request
import _elementtree

offset_increment = 4

def recOutput(element, offset):
    for child in element:
        print(" " * offset + child.tag)
        recOutput(child, offset + offset_increment)

def output(element):
    recOutput(element, 0)

url = "http://mit.spbau.ru/news/rss"
text = (urllib.request.urlopen(url)).read()

tree = _elementtree.fromstring(text)
output(tree)

