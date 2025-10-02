# 콜백 함수: 함수의 매개변수로 사용되는 함수

def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)