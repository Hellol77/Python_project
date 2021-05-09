from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Second_hand_crawler(object):
	def __init__(self,query,page_num):
		self.query = query
		self.page_num =page_num
		self.url=f"https://cafe.naver.com/ca-fe/home/search/c-articles?q={query}&p={page_num}"
		self.driver = webdriver.Chrome('C:/Users/Hellol/Desktop/python practice/Python_project/Crawling/chromedriver.exe')
		
	def load_page(self):
		driver = self.driver
		driver.implicitly_wait(1)
		driver.get(self.url)
		name_data = driver.find_elements_by_class_name("subject_text")
		price_data= driver.find_elements_by_class_name("item_info_area")
		for name,price in zip(name_data,price_data):
			print(name.text)
			print(price.text)
			print('')
			
	def close_web(self):
		self.driver.close()
		
staff=input("중고구매할 제품의 이름을 입력하세요 : ")
for i in range(16):
	crawler=Second_hand_crawler(staff,i)
	crawler.load_page()
	crawler.close_web()
