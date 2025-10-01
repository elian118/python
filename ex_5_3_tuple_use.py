# 튜플은 리스트와 유사하나, 수정이 불가한 자료형

# 튜플을 괄호 생략이 가능하다.
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

# 언패킹(JS의 구조분해할당과 유사한 문법) 적용 가능
a, b, c = 10, 20, 30 # a, b, c = (10, 20, 30)
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)

print("# 리스트와 튜플 언패킹 → 같은 자료형으로만 할당 가능")
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("# 튜플 값 교환")
a, b = 10, 20
print("# 교환 전 값")
print("a:", a)
print("b:", b)
a, b = b, a # 다른 언어와 달리, 파이썬은 값 교환(swap)에 필요한 가공 절차가 불필요
print("# 교환 후 값")
print("a:", a)
print("b:", b)

# 아래는 괄호가 생략된 튜플을 리턴과 즉시 언패킹하는 함수다
print("# 아래는 괄호가 생략된 튜플을 리턴과 즉시 언패킹하는 함수다")
for i, value in enumerate([1, 2, 3, 4, 5, 6]):
    print("{}번째 요소는 {}입니다.".format(i, value))

print()

# 위 함수는 아래와 같은 의미
for (i, value) in enumerate([1, 2, 3, 4, 5, 6]):
    print("{}번째 요소는 {}입니다.".format(i, value))

print()
print("# divmod 함수도 튜플을 반환하므로 튜플 언패킹 가능")
a, b = 97, 40
x, y = divmod(a, b)
print("x:", x)
print("y:", y)

print()

# 참고: 언패킹은 함수 호출 시 가변 매개변수 입력 방식에 많이 활용된다.
print("# 참고: 언패킹은 함수 호출 시 가변 매개변수 입력 방식에 많이 활용된다.")
def add(a,b):
	return a+b

print(add(1,2))
# add([1,2]) #Error!
print(add(*[1,2]))              # a, b = [1, 2]
print(add(**{'a': 1, 'b': 2}))  # a, b = {'a': 1, 'b': 2}

# 파이써닉한 코드는 여기서 참고 → https://facerain.github.io/pythonic-code-guide/