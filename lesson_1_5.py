from checks import check_status, check_time


resp = {"time_ms": 350}
if __name__ == "__main__":
    check_time(resp)
    check_status(resp)