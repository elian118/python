number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""\
          입력한 문자열은 {}입니다.
          {}는 짝수입니다.""".format(number, number))
else:
    print("""\
          입력한 문자열은 {}입니다.
          {}는 홀수입니다.""".format(number, number))
    
# if 조건문과 여러 줄 문자열 출력 방식은 문법적으로 가능하나 코드가 길어지면 가독성이 떨어지며 혼란스러워지기 쉽다

number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는 홀수입니다.""".format(number, number))
    
# 들여쓰기로 구분하는 파이썬에서 위와 같은 여러줄 출력 코드는 실수를 유발할 수 있을 정도로 불편하기 짝이 없다.
# 되도록 한 줄로 쓰길 권한다.

number = int(input("정수 입력> "))

if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는 짝수입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}는 홀수입니다.".format(number, number))

# 부득이한 경우, 
# 1. 아래와 같은 문자열 연결도 고려 가능하다. 주의할 점은 쉼표를 쓰지 않았다는 것이다. → 쉼표를 쓰면 튜플 선언이 됨

test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
)

print("test:", test)
print("type(test):", type(test))

# 2. 이스케이프 개행문자 \n 을 사용해도 가독성이 나아진다.

number = int(input("정수 입력> "))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 홀수입니다."
    ).format(number, number))