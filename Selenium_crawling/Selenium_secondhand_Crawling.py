#네이버 카페에 있는 각종 중고 물품을 selenium으로 크롤링한다
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

class Second_hand_crawler(object):
	def __init__(self,query,page_num):
		self.query = query#물건 이름
		self.page_num =page_num#1페이지 부터 15페이지 까지 검색할 예정
		self.url=f"https://cafe.naver.com/ca-fe/home/search/c-articles?q={query}&p={page_num}"
		self.driver = webdriver.Chrome('C:/Users/Hellol/Desktop/Coding/Python_project/Selenium_crawling/chromedriver.exe',options=options)
		
	def load_page(self):
		driver = self.driver
		driver.implicitly_wait(1)
		driver.get(self.url)
		name_data = driver.find_elements_by_class_name("subject_text")#제품 이름
		price_data= driver.find_elements_by_class_name("item_info_area")#가격과 각종 정보들
		
		
		for name,price in zip(name_data,price_data):	
			print(name.text)
			print(price.text)
			print('')
			
	def close_web(self):#열린 웹들을 자동으로 닫게한다
		self.driver.quit()
		
staff=input("중고구매할 제품의 이름을 입력하세요 : ")
page=int(input("몇 페이지를 검색할까요? : "))
for i in range(1,page+1):
	crawler=Second_hand_crawler(staff,i)
	crawler.load_page()
	crawler.close_web()