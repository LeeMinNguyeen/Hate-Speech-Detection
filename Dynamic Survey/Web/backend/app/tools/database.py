from pymongo import MongoClient

class MongoDB:
    def __init__(self, host='localhost', port=27017, db_name='survey'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()

    def test_connection(self):
        try:
            self.client.admin.command('ping')
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False