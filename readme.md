#what is youdao.dict
yuodao.dict is a vim plugin for translation english to simplified chinese for chinese people
#how to install
go to plugin dir. put the file youdao.vim and youdao dir to your vim plugin dir.   
modified the youdao.py in youdao dir:

    6 # put your youdao api key here, you should keep it secret
    7 youdao_key = ''
    8 # put your youdao api keyfrom here
    9 youdao_keyfrom = ''

you should request the youdao translation api key and add to the youdao.py
if you do not want request the youdao key, you can install the pyquery and lxml for python
this plugin also work.
