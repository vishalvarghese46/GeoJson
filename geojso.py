import urllib.request, urllib.parse, urllib.error
import json
import requests
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

myToken = 'c0fd279531e5ab806330'
myUrl = 'https://api.dexcell.com/v3/locations/?limit=500'

head = {'Authorization': 'token {}'.format(myToken)}
response = urllib.request.urlopen(myUrl, headers=head)
print('Retrieving', myUrl)
data = response.read().decode() # read  the xml to data as tring
print('Retrieved', len(data), 'characters')

#try:
js = json.loads(data)
#except:
#    js = None
#if not js or 'status' not in js:
#    print('===Failure to Retrieve===')
#    print(data)
#    continue
print(json.dumps(js, indent=4))
