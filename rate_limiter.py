import time
from collections import defaultdict

class TokenBucketRateLimiter:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.buckets = defaultdict(lambda: {
            "tokens": capacity,
            "last_refill": time.time()
        })

    def allow_request(self, key):
        bucket = self.buckets[key]
        now = time.time()

        elapsed = now - bucket["last_refill"]
        bucket["tokens"] = min(
            self.capacity,
            bucket["tokens"] + elapsed * self.refill_rate
        )
        bucket["last_refill"] = now

        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True
        return False

if __name__ == "__main__":
    limiter = TokenBucketRateLimiter(5, 1)
    user = "user_123"

    for i in range(10):
        print(
            f"Request {i+1}:",
            "allowed" if limiter.allow_request(user) else "blocked"
        )
        time.sleep(0.3)
