import easygui as g
import urllib.request

def main():
    msg = "请填写喵的尺寸"
    title = "下载一只喵"
    fieldNames = ["宽：", "高："]
    fieldValues = []
    size = width, height = 400, 600
    fieldValues = g.multenterbox(msg, title, fieldNames, size)

    while 1:
        if fieldValues == None:
            break
        errmsg = ""

        try:
            width = int(fieldValues[0].strip())
        except:
            errmsg += "宽度必须为整数！"

        try:
            height = int(fieldValues[1].strip())
        except:
            errmsg += "高度必须为整数！"    

        if errmsg == "":
            break
        
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

    url = "http://placekitten.com/g/%d/%d" % (width, height)

    response = urllib.request.urlopen(url)
    cat_img = response.read()

    filepath = g.diropenbox("请选择存放喵的文件夹")

    if filepath:
        filename = '%s/cat_%d_%d.jpg' % (filepath, width, height)
    else:
        filename = 'cat_%d_%d.jpg' % (width, height)

    with open(filename, 'wb') as f:
        f.write(cat_img)

if __name__ == "__main__":
    main()
