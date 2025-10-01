import module_basic.test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# 파이썬은 현재 파일이 위치한 곳 기준으로 import 경로를 찾는다.
# 하위 폴더 안에 위치한 모듈에 접근할 경우, [폴더.모듈파일명] 형식으로 접근한다.
# 상대경로로 접근도 가능하다. [..폴더명.폴더명.모듈파일명]