from upstash_redis import Redis
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve environment variables
UPSTASH_ENDPOINT = os.getenv('UPSTASH_ENDPOINT')
UPSTASH_PASSWORD = os.getenv('UPSTASH_PASSWORD')

class RedisClient:
    def __init__(self, url=UPSTASH_ENDPOINT, token=UPSTASH_PASSWORD):
        self.client = Redis(url=url, token=token)

    def set(self, key, value):
        self.client.set(key, value)

    def list_set(self, key, value):
        self.client.rpush(key, value)

    def get(self, key):
        return self.client.get(key)
    
    def list_get(self, key):
        return self.client.lrange(key, 0, -1)

    def delete(self, key):
        self.client.delete(key)

    def exists(self, key):
        return self.client.exists(key)
    
    def disconnect(self):
        self.client.close()

if __name__ == "__main__":
    pass