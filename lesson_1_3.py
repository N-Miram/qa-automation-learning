def get_ids(users):
    ids = []
    for user in users:
        ids.append(user["id"])
    return ids


def get_names(users):               
    names = []
    for user in users:
        names.append(user["name"])
    return names


def check_unique_ids(users):
    ids = get_ids(users)                  
    assert len(ids) == len(set(ids)), f"Есть дубли id: {ids}"


def is_success(response, expected_codes):
    return response["status_code"] in expected_codes


def check_status(response, expected_codes):
    assert is_success(response, expected_codes), f"expected {expected_codes}, actual {response['status_code']}"


users = [{"id": 1, "name": "Anna"}, {"id": 2, "name": "Boris"}]
print(get_names(users))     # ['Anna', 'Boris']

print(is_success({"status_code": 201}, (200, 201, 204)))   # True
print(is_success({"status_code": 500}, (200, 201, 204)))   # False

users_ok  = [{"id": 1}, {"id": 2}, {"id": 3}]
users_bad = [{"id": 1}, {"id": 2}, {"id": 1}]

check_unique_ids(users_ok)     # молча
#check_unique_ids(users_bad)    # падает 


check_status({"status_code": 201}, (200, 201, 204))    # молча
check_status({"status_code": 500}, (200, 201, 204))    # падает

