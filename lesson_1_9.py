from api_response import ApiResponse


fast = ApiResponse(200, 350)
slow = ApiResponse(500, 2000)

fast.check_status(200)
fast.check_time()
print("fast: проверки прошли")

slow.check_time(limit=1000)