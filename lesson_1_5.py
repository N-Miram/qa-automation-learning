def check_time(response, limit=1000):
    try:
        actual = response["time_ms"]
    except KeyError:
        raise AssertionError("в ответе нет поля time_ms")
    assert actual <= limit, f"expected <= {limit}, actual {actual}"


def check_status(response, expected=200):
    try:
        actual = response["status_code"]
    except KeyError:
        raise AssertionError("в ответе нет поля status_code")
    assert actual == expected, f"expected == {expected}, actual {actual}"


resp = {"time_ms": 350}
    
check_time(resp)
check_status(resp)