def check_time(response, limit=1000):
    assert response["time_ms"] <= limit, f"expected <= {limit}, actual {response['time_ms']}"


resp = {"status_code": 200, "time_ms": 1350}

# check_time(resp)
# check_time(resp, limit=2000) 

def add_error(text, errors=None):
    if errors is None:
        errors = []
    errors.append(text)
    return errors


print(add_error("нет email"))
print(add_error("нет id"))