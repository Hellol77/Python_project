#네이버 뉴스를 크롤링
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

query= urllib.parse.quote_plus(input('뉴스의 주제를 입력하세요 : '))
page_num=int(input('검색할 페이지수를 입력하세요 : '))
for i in range (1,page_num*10-9):
	url="https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=70&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page_num}}"
	html = urllib.request.urlopen(url).read()
	soup= BeautifulSoup(html,'html.parser')
	title = soup.find_all(class_='info')
	for i in title:
		print(i.attrs['href'])                                                                                                                           
