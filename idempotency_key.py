import time
import uuid


class IdempotencyStore:
    def __init__(self):
        self.store = {}

    def get(self, key):
        record = self.store.get(key)
        if not record:
            return None

        if time.time() > record["expires_at"]:
            del self.store[key]
            return None

        return record["response"]

    def save(self, key, response, ttl_seconds=300):
        self.store[key] = {
            "response": response,
            "expires_at": time.time() + ttl_seconds
        }


class PaymentService:
    def __init__(self):
        self.store = IdempotencyStore()

    def process_payment(self, amount, idempotency_key):
        existing = self.store.get(idempotency_key)
        if existing:
            print("Returning cached response.")
            return existing

        transaction_id = str(uuid.uuid4())

        response = {
            "status": "success",
            "transaction_id": transaction_id,
            "amount": amount
        }

        self.store.save(idempotency_key, response)
        print("Processed new payment.")
        return response


if __name__ == "__main__":
    service = PaymentService()
    key = "abc123"

    print(service.process_payment(100, key))
    print(service.process_payment(100, key))