# 파이썬은 문자열을 하나의 완성된 리스트로 간주한다.

print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
print()

print("문자를 뒤에서부터 선택해볼까요?")
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])
print()

# 따라서, 배열에서 사용하는 범위 선택 연산자 사용도 가능하다
print("안녕하세요"[1:4]) # 1부터 3까지 인덱스 출력 → arr[x, y]: x부터 뒤에 숫자 (y -1)까지를 범위로 포함
print("안녕하세요"[1:]) # 1부터 끝까지 인덱스 출력
print("안녕하세요"[:3]) # 처음부터 2까지 인덱스 출력
print()

# 선언된 문자열 범위 외 인덱스로 접근하면 string index out of range 오류가 발생한다.
# print("안녕하세요"[10])

# Traceback (most recent call last):
#   File "C:\Users\USER\Desktop\hancom\python\ex_1_string_operator01.py", line 26, in <module>
#     print("안녕하세요"[10])
#           ~~~~~~~~~~~~^^^^
# IndexError: string index out of range

# 문자열 길이는 len 함수로 간단히 구할 수 있다.

print(len("안녕하세요"))