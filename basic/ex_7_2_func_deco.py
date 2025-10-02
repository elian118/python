# 로거로 사용될 수 있는 함수 데코레이터 예제
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()

# 데코레이터는 크게 함수 데코레이터와 클래스 데코레이터로 구분된다.
# 함수 데코레이터는 함수에 사용되는 데코레이터로, 
# 대상 함수 앞뒤에 꾸밀 부가적 내용 혹은 반복할 내용을 먼저 정의해 손쉽게 사용할 수 있도록 한 것을 말한다.