from bs4 import BeautifulSoup

b=BeautifulSoup(open(r'G:\work\wuzimeide\shiyong.html'))
print b.prettify('utf-8')