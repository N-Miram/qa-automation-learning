response = {
    "status_code": 200,
    "body": {
        "total": 3,
        "users": [
            {"id": 1, "name": "Anna",  "email": "anna@test.com",  "roles": ["user"]},
            {"id": 2, "name": "Bor", "email": "boris@test.com", "roles": ["user", "admin"]},
            {"id": 3, "name": "Clara", "email": "clara@test.com", "roles": ["user"]},
        ],
    },
}
users= response["body"]["users"]
assert response["status_code"] == 200
assert response["body"]["total"] == len(response["body"]["users"])
assert response["body"]["users"][1]["name"] == "Boris"
assert "admin" in response["body"]["users"][1]["roles"]


for user in users:
    assert "@" in user["email"] , f"Нет @ в email у пользователя {user['name']}"

assert "password" not in users[0] 
   



print("Все проверки пройдены")