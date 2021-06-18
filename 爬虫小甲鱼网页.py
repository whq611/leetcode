import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://ilovefishc.com')
html = response.read()
html = html.decode('utf-8')
print(html)
