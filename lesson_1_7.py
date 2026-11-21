import json
from lesson_1_5 import check_status

def parse_body(body):
    try:
        result = json.loads(body)     
    except json.JSONDecodeError:         
        raise AssertionError("в ответе нет json body")       
    return result


check_status(parse_body('{"status_code": 200}'))
print("проверка прошла")