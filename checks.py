import json
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


def parse_body(body):
    try:
        result = json.loads(body)     
    except json.JSONDecodeError:         
        raise AssertionError("в ответе нет json body")       
    return result