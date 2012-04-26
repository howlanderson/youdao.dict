import urllib2
import urllib
import json
import sys

# put your youdao api key here, you should keep it secret
youdao_key = ''
# put your youdao api keyfrom here
youdao_keyfrom = ''

if not youdao_key:
    from pyquery import PyQuery as pq
    from lxml import etree
    word = sys.argv[1]
    youdao_url = 'http://dict.youdao.com/search?q=' + word + '&keyfrom=dict.index#q%3Dtest%26keyfrom%3Ddict.index'
    try:
        d = pq(url=youdao_url)
        p = d("div#results-contents div.trans-container  ul:first")
        print (p.text().encode("utf-8","ingnore"))
    except Exception, e:
        print 'some error happened'
        sys.exit()
else:
    word = sys.argv[1]
    youdao_url = 'http://fanyi.youdao.com/openapi.do?keyfrom=' + youdao_keyfrom + '&key=' + youdao_key + '&type=data&doctype=json&version=1.1&q=' + word
    try:
        req = urllib2.Request(url = youdao_url)
        f = urllib2.urlopen(req)
        json_data = f.read()
        json_object = json.loads(json_data)
    except Exception, e:
        print 'some error happened'
        sys.exit()
    if not json_object['errorCode']: 
        try:
            translation_result = json_object['basic']['explains']
        except Exception, e:
            print 'some error happened'
            sys.exit()
        print (''.join(translation_result)).encode('utf-8', 'ignore')
    else:
        print 'api return error'
