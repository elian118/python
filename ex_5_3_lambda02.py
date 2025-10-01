# 인라인 람다: 함수 선언 과정 없이 한 줄로 작성된 람다 함수를 매개변수로 입력하는 방식

list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print()

# 즉, 이렇게 쓸라고 람다를 만든 것임
# 인라인 람다는 연산 과정을 코드 그 자체로 내포하고 있어 의미전달에 유용하지만, 너무 수식이 길어지면 오히려 의미전달이 어려울 수 있다.
# 이런 경우는 그냥 일반 함수를 선언해 가져다 쓰는 편이 좋다.