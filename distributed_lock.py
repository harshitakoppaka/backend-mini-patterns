import threading
import time


class DistributedLock:
    def __init__(self):
        self._lock = threading.Lock()
        self.locked_until = 0

    def acquire(self, ttl_seconds=5):
        with self._lock:
            current_time = time.time()

            # If lock expired, allow acquisition
            if current_time > self.locked_until:
                self.locked_until = current_time + ttl_seconds
                return True

            return False

    def release(self):
        with self._lock:
            self.locked_until = 0


if __name__ == "__main__":
    lock = DistributedLock()

    if lock.acquire(ttl_seconds=3):
        print("Lock acquired. Processing resource...")
        time.sleep(2)
        lock.release()
        print("Lock released.")
    else:
        print("Could not acquire lock.")