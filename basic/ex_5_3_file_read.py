# with: 파일을 open() 하면 반드시 close()해야 하는 상용구를 줄여주는 예약어
# close()를 누락하는 실수를 미연에 방지할 수 있다.

with open("basic.txt", "r") as file:
    contents = file.read()

print(contents)

# contents는 with 구문 안에 선언된 지역변수이나, print(contents)를 통해 접근이 가능하다
# with 구문은 파일의 open() close()만 대신해줄 뿐이며 함수가 아니다. 따라서 실체는 처음부터 파일 스코프 안에서 작동했던 아래 코드의 함축문이라고 봐야 한다.

# file = open("basic.txt", "r")
# contents = file.read()
# file.close()

# print(contents)

# 이렇게 보면 contents 변수는 애초부터 현재 파일 스코프에 속해 있었던 셈이다.
# 따라서 같은 스코프 안에 있는 출력문에서 접근이 가능한 것이다.

print()
# 참고: 현재 스코프에 존재하는 지역변수 정보는 아래와 같이 확인 가능하다.
print(locals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D00AFCCD10>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\USER\\Desktop\\hancom\\python\\ex_5_3_file_read.py', '__cached__': None, 'file': <_io.TextIOWrapper name='basic.txt' mode='r' encoding='cp949'>, 'contents': 'Hello Python Programmin...!'}