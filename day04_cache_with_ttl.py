import time

class TTLCache:
    def __init__(self):
        self.store = {}

    def set(self, key, value, ttl_seconds):
        expire_time = time.time() + ttl_seconds
        self.store[key] = (value, expire_time)

    def get(self, key):
        if key not in self.store:
            return None

        value, expire_time = self.store[key]

        if time.time() > expire_time:
            del self.store[key]
            return None

        return value


if __name__ == "__main__":
    cache = TTLCache()

    cache.set("user_1", {"name": "Harshita"}, ttl_seconds=3)

    print("First fetch:", cache.get("user_1"))

    time.sleep(4)

    print("After expiration:", cache.get("user_1"))