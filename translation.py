import urllib.request
import urllib.parse
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
content = input('请输入需要翻译的内容:')
url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '16259864748896'
data['sign'] = '4321a40dfa37c385bc67b553eb3d3b09'
data['lts'] = '1625986474889'
data['bv'] = '35b48b2871e19cf5e4fb073019371d86'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
target = json.loads(html)
print('翻译结果: %s' %(target['translateResult'][0][0]['tgt']))

