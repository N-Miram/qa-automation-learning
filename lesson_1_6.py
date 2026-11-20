import json  # подключаем встроенный модуль для работы с JSON

body = '{"status_code": 200, "time_ms": 350}'


data = json.loads(body)
print(type(data))
print(data["status_code"])


print(type(body))  # <class 'str'>


user = {"name": "Miram", "age": 30}
text = json.dumps(user)
print(type(text))
print(text)
print(user)


with open("user.json") as f:   # открыть файл; f — «ручка» к файлу
    user_from_file = json.load(f)   # load БЕЗ s: читает из файла, а не из строки

print(type(user_from_file))
print(user_from_file["role"])