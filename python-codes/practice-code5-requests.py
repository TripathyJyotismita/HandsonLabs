>>> import requests
>>> req = requests.request('GET', 'https://httpbin.org/get')
>>> req
<Response [200]>


>>> import requests
>>> s = requests.Session()
>>> s.get('https://httpbin.org/get')
<Response [200]>

Or as a context manager:

>>> with requests.Session() as s:
...     s.get('https://httpbin.org/get')
<Response [200]>

>>> import requests
>>> req = requests.Request('GET', 'https://httpbin.org/get')
>>> req.prepare()
<PreparedRequest [GET]>

API Changes¶
Response.json is now a callable and not a property of a response.

import requests
r = requests.get('https://github.com/timeline.json')
r.json() 

proxies = {
  "http": "10.10.1.10:3128",    # use http://10.10.1.10:3128 instead
}
requests.get("http://example.org", proxies=proxies)


=====================================================

import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']

==================================================================
import urllib2

gh_url = 'https://api.github.com'

req = urllib2.Request(gh_url)
password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'pass')

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(req)

print handler.getcode()
print handler.headers.getheader('content-type')

---------------
