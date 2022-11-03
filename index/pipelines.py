import json

class XmetaPipeline:
    def __init__(self):
        self.file = open('shuju.txt', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(item, ensure_ascii=False) + '\n')#写入数据到文件
        return item