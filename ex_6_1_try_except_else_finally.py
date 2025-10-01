pi = 3.14

try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * pi * number_input_a)
    print("원의 넓이:", pi * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

# 위 방식은 먼저 로직을 실행하고 예외를 포함한 실행 결과를 로그로 출력하도록 설계됐다.