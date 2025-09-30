# 가변 매개변수: 매개변수를 원하는 만큼 받을 수 있는 함수

# 가변 매개변수 뒤에는 일반 매개변수가 올 수 없음
# 가변 매개변수는 맨 뒤에 하나만 사용 가능 → 전개연산자로 표현

# def 함수명(매개변수, 매개변수, ..., *가변 매개변수):
#   문장

def print_n_times(m, *values):
    for i in range(m):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")