import urllib.request
import chardet
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
def main():
    url = input("请输入URL：")

    response = urllib.request.urlopen(url)
    html = response.read()

    # 识别网页编码
    encode = chardet.detect(html)['encoding']
    if encode == 'GB2312':
        encode = 'GBK'

    print("该网页使用的编码是：%s" % encode)
        
if __name__ == "__main__":
    main()
