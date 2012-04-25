from pyquery import PyQuery as pq
from lxml import etree
import urllib
import sys

word = sys.argv[1]
youdao_url = 'http://dict.youdao.com/search?q=' + word + '&keyfrom=dict.index#q%3Dtest%26keyfrom%3Ddict.index'
d = pq(url=youdao_url)
p = d("div#results-contents div.trans-container  ul:first")
print(p.text().encode("utf-8","ingnore"))
