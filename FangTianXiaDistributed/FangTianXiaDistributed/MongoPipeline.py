# author:dayin
# Date:2019/12/18 0018

from pymongo import MongoClient

from FangTianXiaDistributed.items import NewHouseItem, OldHouseItem


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        # 新房和二手房的数据分开存放
        if isinstance(item, NewHouseItem):
            self.db['newHouse'].insert(dict(item))
            print('[success] insert into the newHouse : ' + item.get('name') + ' to MongoDB')
        elif isinstance(item, OldHouseItem):
            self.db['oldHouse'].insert(dict(item))
            print('[success] insert into the oldHouse : ' + item.get('name') + ' to MongoDB')
        return item

    def close_spider(self, spider):
        self.client.close()
