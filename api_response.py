class ApiResponse:
    def __init__(self, status_code, time_ms):
        self.status_code = status_code
        self.time_ms = time_ms

    def check_status(self, expected):
        if self.status_code != expected:
            raise AssertionError(f"ожидали {expected}, получили {self.status_code}")

    def check_time(self, limit=1000):
        if self.time_ms > limit:
            raise AssertionError(f"ответ пришел за {self.time_ms}ms, лимит {limit}ms")