from checks import check_status, parse_body


check_status(parse_body('{"status_code": 200}'))
print("проверка прошла")