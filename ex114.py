''' Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URlError:
    print('deu erro')
else:
    print('ok')
    #print(site.read())
