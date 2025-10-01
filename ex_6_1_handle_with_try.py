pi = 3.14

try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * pi * number_input_a)
    print("원의 넓이:", pi * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.") # 오류 메시지 없이 프로그램 중단만 막고 싶다면 pass로 대체해도 된다.