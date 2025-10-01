from test_package import *

print(module_a.variable_a)
print(module_b.variable_b)

# __init__ → 특정 폴더에 위치한 모든 모듈 모음(패키지)의 정의를 통해 모듈을 가져와 사용하는 형태
# from 패키지(폴더)명 import * 을 사용하려면 반드시 __init__.py 파일이 필요하다.
# 패키지 폴더 안에 __init__.py 파일이 존재하면 import로 접근 시 먼저 __init__.py가 실행된다.

# 참고 - 파일명.cpython.pyc 파일
# 모듈을 사용할 때 파이썬 가상머신에서 자동으로 생성하는 미리 컴파일된 캐시파일이며 __pycache__ 폴더 안에 위치한다.
# 삭제해도 실행에 문제가 없지만 어차피 실행 시 또 생성된다.