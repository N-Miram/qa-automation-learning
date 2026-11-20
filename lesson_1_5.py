resp = {"status_code": 200, "time_ms": 350}


def check_time(response, limit=1000):
    try:
        actual = response["time_ms"]
    except KeyError:
        raise AssertionError("в ответе нет поля time_ms")
    assert actual <= limit, f"expected <= {limit}, actual{actual}"


check_time(resp)