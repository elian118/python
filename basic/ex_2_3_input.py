# 파이썬의 input함수는 오로지 문자열 객체로 간주된다.
string = input("입력> ")
print("자료: ", string)
print("자료형: ", type(string))

# 따라서 숫자 간 계산을 의도한 거라면 반드시 입력값의 형변환을 먼저 처리하고 난 후 계산해야 한다.

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b) # 형변환된 숫자로 계산

# int()함수와 float() 함수 조합하기
input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

# ValueError
# 1. 숫자가 아닌 것을 숫자로 변환하려고 할 때
# int("안녕하세요")
# float("안녕하세요")

# 2. 소수점이 있는 숫자 형식의 문자열을 int()함수로 변환하려고 할 때
# int("52.273")

# 숫자를 문자열로 바꾸기
output_a = str(52)
output_b = str(52.273)
print(type(output_a), output_a)
print(type(output_b), output_b)

# inch → cm
raw_input = input("inch 단위 숫자를 입력해주세요: ")

inch = int(raw_input)
cm = inch * 2.54

print(inch, "inch는 cm 단위로", cm, "cm입니다.")