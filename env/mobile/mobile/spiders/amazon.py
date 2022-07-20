import scrapy
from ..items import MobileItem

# Scrap Data From Amazon Website
class AmazonSpider(scrapy.Spider):
	name = 'amazon'
	start_urls = [
		'https://www.amazon.in/s?k=mobile&rh=n%3A1389401031&ref=nb_sb_noss'
	]
	page_number = 1
	while page_number < 6:
		page_number += 1
		start_urls.append("https://www.amazon.in/s?k=mobile&i=electronics&rh=n%3A1389401031&page="+str(page_number)+"&qid=1628075150&ref=sr_pg_2")

	def parse(self,response):

		items = MobileItem()

		title = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-size-medium", " " )) and contains(concat( " ", @class, " " ), concat( " ", "a-text-normal", " " ))]/text()').extract()
		price = response.xpath('//*[(@id = "search")]//*[contains(concat( " ", @class, " " ), concat( " ", "a-price-whole", " " ))]/text()').extract()
		page = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-selected", " " ))]//a/text()').extract()
		

		for item in zip(title,price):
			items['title'] = item[0]
			items['price'] = item[1]
			items['page'] = page
			
			
			yield items
