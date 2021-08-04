# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class MobilePipeline:
	def __init__(self):
		self.model = [
			'Samsung Galaxy M32 (Light Blue, 6GB RAM, 128GB Storage)',
			'Gionee',
			'iQOO Z3 5G (Ace Black, 6GB RAM, 128GB Storage)',
			'realme C11',

		]
		self.create_conn()
		self.create_table()

	def create_conn(self):
		self.con = sqlite3.connect('mobile.db')
		self.cur = self.con.cursor()

	def create_table(self):
		self.cur.execute(""" DROP TABLE IF EXISTS product_tb""")
		self.cur.execute(""" CREATE TABLE product_tb(
				title text,
				price text,
				page text
			)""")

	def process_item(self, item, spider):
		self.store_db(item)
		return item

	def store_db(self,item):
		for text in self.model:
			if text in item['title']:
				self.cur.execute(""" INSERT INTO product_tb VALUES(?,?,?)""",(item['title'],item['price'],item['page'][0]))
				self.con.commit()

