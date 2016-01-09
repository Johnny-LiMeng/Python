import urllib.request  
url = "http://clsq.co/htm_mob/8/1601/1791248.html"  
def addheaders(url):
    headers = ('User-Agent',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()  
    opener.addheaders = [headers]  
    data = opener.open(url).read()  
    mystr = data.decode("utf8")
    return mystr

path="C:/work/1111.txt"
with open(path, 'w') as f:
    f.write(addheaders(url))  