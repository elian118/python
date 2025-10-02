# 예외 객체는 여럿이지만, 예외처리 도중 예상치 못한 예외가 발생하면 어떤 케이스도 걸리지 않아 결국 프로그램이 종료된다.
# 이를 방지하려면 가장 맨 아래 최상위 예외 객체 Exception에 대한 예외처리를 추가해주는 편이 좋다.

list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요() # 고의적 예외 발생
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print("type(exception)", type(exception))
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!") 
    print("type(exception)", type(exception))
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.") 
    print("type(exception)", type(exception))