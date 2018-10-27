import redis

class RedisWrapper():

    def initRedis(self):
        self.r = redis.Redis(host = "localhost", port = "6379")

    def insert(self, key, value):
        if not self.r.get(key):
            return self.r.set(key, value) # returns True if success
        return False

    def get(self, key):
        return self.r.get(key)