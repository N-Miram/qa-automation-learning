users_ok  = [{"id": 1}, {"id": 2}, {"id": 3}]
users_bad = [{"id": 1}, {"id": 2}, {"id": 1}]

def check_unique_ids(users):
    ids = []
    for user in users:
        ids.append(user["id"])

    assert len(ids) == len(set(ids)), f"Есть дубли id: {ids}"

check_unique_ids(users_ok)    # внутри users = users_ok
check_unique_ids(users_bad)   # внутри users = users_bad