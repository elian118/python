list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 출력
print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)
print()

# 기본 연산자
print("# 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

# 함수
print("# 길이 구하기")
print("len(list_a) =", len(list_a))
print("len(list_a + list_b) =", len(list_a + list_b))
print()

# 파이썬의 list는 다른 언어의 배열과 다른 자료형이다.
# 리스트는 요소로 아무 자료형이나 다 담을 수 있지만, 배열은 같은 자료형만 담을 수 있다. 이는 메모리 저장 주소가 요소 순서대로 연속되는 배열의 태생적 구조 때문이다.
# list_a + list_b 연산은 원본 배열 list_a, list_b를 변형하지 않는다.
# 반면에, list_a.extend(list_b)는 결합 후 원본 배열에 각각에 결합한 값을 대입하므로 원본이 변형된다.