import mysql.connector
import scrapy
from mysql.connector import errorcode
import datetime



# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


#class ScrapyprojectPipeline:
 #   def process_item(self, item, spider):
  #
#      return item

class CoreymsPipeline():


    collection_name = 'scrapy_items'
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'web_scraping',
        'raise_on_warnings': True
    }
    add_post = ("INSERT INTO web_scraping.coreyms"
                 "(summary, link) "
                 "VALUES (%s, %s)")

    def __init__(self):
       print(self.config.items())



    def open_spider(self, spider):
        try:
            self.cnx = mysql.connector.connect(**self.config)
            self.cursor = self.cnx.cursor()
        except  mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    # def close_spider(self, spider):
    #     self.cnx.close()

    def process_item(self, item, spider):
        # print("************text**********", item['text'])
        # print("************author**********", item['author'])
        # print("************tags**********", item['tags'])
        try:
            self.cursor.execute(self.add_post, (item['summary'].encode('utf-8'),
                                                 item['link'].encode('utf-8'),
                                                ))
            self.cnx.commit()
            print("\ninserted--->", item)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        return item




class MySQLPipeLine():
    collection_name = 'scrapy_items'
    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'web_scraping',
        'raise_on_warnings': True
    }

    add_quote = ("INSERT INTO web_scraping.quotes"
                 "(quote, author, tags, last_upd_timestampquotes) "
                 "VALUES (%s, %s, %s, %s)")

    def __init__(self):
        print(self.config.items())

    def open_spider(self, spider):
        try:
            self.cnx = mysql.connector.connect(**self.config)
            self.cursor = self.cnx.cursor()
        except  mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def process_item(self, item, spider):
        # print("************text**********", item['text'])
        # print("************author**********", item['author'])
        # print("************tags**********", item['tags'])
        tags = self.list_to_string(item['tags'])
        try:
            self.cursor.execute(self.add_quote, (item['text'].encode('utf-8'),
                                                 item['author'].encode('utf-8'),
                                                 tags.encode('utf-8'),
                                                 self.get_time_now()))

            self.cnx.commit()
            print("\ninserted--->", item)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        return item

    def list_to_string(self, s):
        # initialize an empty string
        str1 = ""
        # traverse in the string
        for ele in s:
            str1 += ele
            # return string
        return str1

    def get_time_now(self):
        now = datetime.datetime.utcnow()  # now()
        today_now = now.strftime("%Y-%m-%d %H:%M:%S")
        return today_now
