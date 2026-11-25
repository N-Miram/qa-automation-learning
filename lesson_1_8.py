class TestCase:                      
    def __init__(self, tc_id, title):  
        self.tc_id = tc_id          
        self.title = title

    def show(self):
        print(f"{self.tc_id}: {self.title}")


tc1 = TestCase("TC-15", "Логин")     
tc2 = TestCase("TC-16", "Выход")     
tc3 = TestCase("TC-17", "Регистрация") 


tc1.show()   
tc2.show()   
tc3.show()


class ApiResponse:
    def __init__(self, status_code, time_ms):
        self.status_code = status_code
        self.time_ms = time_ms
        
    def check_status(self, expected):
        if self.status_code != expected:
            raise AssertionError(f"ожидали {expected}, получили {self.status_code}")


resp = ApiResponse(200, 350)

resp.check_status(200)
print("проверка 200 прошла")
resp.check_status(404)