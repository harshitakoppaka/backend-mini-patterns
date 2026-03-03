# Backend Mini Patterns

A collection of reusable backend system design patterns implemented in Python.

These patterns focus on common production-ready concepts used in scalable backend systems.

## Included Patterns

### Pagination Helper
Utility for paginating large datasets in API responses.

### Token Bucket Rate Limiter
Implements request throttling using the token bucket algorithm to control API traffic.

### Retry with Exponential Backoff
Handles transient failures when calling unreliable external services.

### TTL Cache (In-Memory)
Implements time-based caching to reduce redundant computation and improve performance.
### Circuit Breaker Pattern
Implements failure detection and recovery logic to prevent cascading failures in distributed systems.
## 🔐 Idempotency Key Pattern – Example Usage

```python
from idempotency_key import IdempotencyStore

store = IdempotencyStore()

request_key = "user-123-payment-456"

if store.exists(request_key):
    print("Duplicate request detected")
else:
    store.save(request_key)
    print("Processing request...")