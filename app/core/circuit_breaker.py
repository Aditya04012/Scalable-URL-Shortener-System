import asyncio
import time

class CircuitBreaker:
    def __init__(self, fail_threshold=5, reset_timeout=10):
        self.fail_count = 0
        self.fail_threshold = fail_threshold
        self.reset_timeout = reset_timeout
        self.last_failed_time = None
        self.state = "CLOSED"

    def can_call(self):
        if self.state == "OPEN":
            if time.time() - self.last_failed_time > self.reset_timeout:
                self.state = "HALF_OPEN"
                return True
            return False
        return True

    def record_success(self):
        self.fail_count = 0
        self.state = "CLOSED"

    def record_failure(self):
        self.fail_count += 1
        if self.fail_count >= self.fail_threshold:
            self.state = "OPEN"
            self.last_failed_time = time.time()


circuit = CircuitBreaker()