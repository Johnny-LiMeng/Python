import re
import urllib.request

def addheaders(url):  #模仿成浏览器访问（以免被拒），并得到解码的页面内容
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')   
    opener = urllib.request.build_opener()  
    opener.addheaders = [headers]  
    data = opener.open(url).read()  
    mystr = data.decode("utf8")
    return mystr

def getImg(html):  #找出页面内容中的jpg图片并保存
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    i = 0  
    for imgurl in imglist:
        add = "C:\work\photos\%s.jpg" %i   #图片保存的地址
        urllib.request.urlretrieve(imgurl, add)  
        i+=1

url = "http://tieba.baidu.com/p/2166231880" 
html = addheaders(url) 
getImg(html)
path="C:/work/1335.txt" #页面内容保存的地址
with open(path, 'w') as f:
    f.write(mystr)