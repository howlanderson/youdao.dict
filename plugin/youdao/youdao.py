import urllib2
import urllib
import json
import sys

youdao_key = '1845492630'
youdao_keyfrom = 'howlanderson'

if not youdao_key:
    from pyquery import PyQuery as pq
    from lxml import etree
    word = sys.argv[1]
    youdao_url = 'http://dict.youdao.com/search?q=' + word + '&keyfrom=dict.index#q%3Dtest%26keyfrom%3Ddict.index'
    d = pq(url=youdao_url)
    p = d("div#results-contents div.trans-container  ul:first")
    print(p.text().encode("utf-8","ingnore"))
else:
    word = sys.argv[1]
    youdao_url = 'http://fanyi.youdao.com/openapi.do?keyfrom=' + youdao_keyfrom + '&key=' + youdao_key + '&type=data&doctype=json&version=1.1&q=' + word
    req = urllib2.Request(url = youdao_url)
    f = urllib2.urlopen(req)
    json_data = f.read()
    json_object = json.loads(json_data)
    if not json_object['errorCode']: 
        try:
            translation_result = json_object['basic']['explains']
        except Exception, e:
            print 'some error happen'
            sys.exit()
        print (''.join(translation_result)).encode('utf-8', 'ignore')
    else:
        print 'api return error'
