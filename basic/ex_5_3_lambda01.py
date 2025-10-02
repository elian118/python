# 파이썬의 람다 함수는 아래와 같은 형식으로 한 줄 이내로 더 간결하게 만든 함수를 의미한다.
# lambda 함수로 전환이 될 수 있는 대상 함수는 반드시 결과 리턴문이 존재해야 한다.
# 따라서, 파이썬 3항식도 lambda 표현이 가능하다.
# lambda 예약어가 필요하며, 표현이 간단해 유용하다. 단, 너무 긴 함수를 람다로 표현하는 건 오히려 역효과다.

# def power(item): return item * item
power = lambda x: x * x

# def under_3(item): return item < 3
under_3 = lambda x: x < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)        # map() → object 자료형으로 반환하므로, 즉시 확인 불가 
print("map(power, list_input_a):", list(output_a))  # list 자료형으로 형변환 후 확인 가능
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)       # filter() → object 자료형으로 반환하므로, 즉시 확인 불가 
print("filter(under_3, list_input_a):", list(output_b)) # list 자료형으로 형변환 후 확인 가능
print()

# 람다는 매개변수가 여럿인 것도 선언 가능하다.
# lambda x, y: x * y

# 즉, lambda 매개변수(들): 로직 형태로 선언