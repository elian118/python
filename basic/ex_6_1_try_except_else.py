pi = 3.14

try:
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * pi * number_input_a)
    print("원의 넓이:", pi * number_input_a * number_input_a)
# finally:
    # print("program end")

# 위 방식은 예외 발생이 없으면 후속 로직을 실행하겠다는 의도가 있다.