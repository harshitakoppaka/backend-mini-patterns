import time
import random


def retry_with_backoff(func, retries=5, base_delay=1):
    """
    Retries a function using exponential backoff.
    """
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == retries:
                raise

            delay = base_delay * (2 ** (attempt - 1))
            print(
                f"Attempt {attempt} failed: {e}. "
                f"Retrying in {delay} seconds..."
            )
            time.sleep(delay)


# Example usage
def flaky_service():
    if random.random() < 0.7:
        raise Exception("Temporary failure")
    return "Success!"


if __name__ == "__main__":
    result = retry_with_backoff(flaky_service)
    print("Result:", result)
