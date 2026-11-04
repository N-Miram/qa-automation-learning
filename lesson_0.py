def is_valid_status(code):
    return code >= 200 and code <= 299
   


# Проверки: если всё верно, программа напечатает "Все проверки пройдены"
assert is_valid_status(200) == True
assert is_valid_status(201) == True
assert is_valid_status(299) == True
assert is_valid_status(199) == False
assert is_valid_status(300) == False
assert is_valid_status(404) == False
print("Все проверки пройдены")