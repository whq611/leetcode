import random
class Codec:
    def __init__(self):
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.a = {}
    
    def encode(self,long_url):
        key = ''.join(random.sample(self.chars,6))
        while self.a.get(key):
            key = ''.join(random.sample(self.chars,6))
        self.a[key] = long_url
        return 'http://tinyurl.com/' + key
    def decode(self,short_url):
        return self.a[short_url[19:]]
