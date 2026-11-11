def check_unique_ids(users):
    ids = []
    for user in users:
        ids.append(user["id"])

    assert len(ids) == len(set(ids)), f"Есть дубли id: {ids}"


def check_required_fields(user, required):
    missing = required - set(user)         # чего не хватает: используйте REQUIRED, set(user) и минус

    assert missing == set(), f" net poley {missing}"


def check_status(response, expected_codes):
   assert response["status_code"] in expected_codes, f"expected {expected_codes}, actual {response["status_code"]}" 


users_ok  = [{"id": 1}, {"id": 2}, {"id": 3}]
users_bad = [{"id": 1}, {"id": 2}, {"id": 1}]


REQUIRED = {"id", "name", "email"}
anna  = {"id": 1, "name": "Anna", "email": "a@test.com"}
boris = {"id": 2, "name": "Boris"}


SUCCESS_CODES = (200, 201, 204)
ok_response  = {"status_code": 201}
bad_response = {"status_code": 500}


check_unique_ids(users_ok)    # внутри users = users_ok
#check_unique_ids(users_bad)   # внутри users = users_bad


check_required_fields(anna, REQUIRED)     # молча
#check_required_fields(boris, REQUIRED)    # падает: {'email'}


check_status(ok_response, SUCCESS_CODES)     # молча
check_status(bad_response, SUCCESS_CODES)    # падает