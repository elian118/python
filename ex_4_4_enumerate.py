example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print("# list() 함수 강제 변환 출력")
print(list(enumerate(example_list))) # 인덱스 번호가 요소마다 박혀져 있고(튜플), 리스트로 강제 변환했을 때 확인 가능
print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))
print()

# enumerate 외 리스트로 강제 형변환해야 요소를 확인할 수 있는 특수 객체로는 Iterater가 있다.

# 원본 리스트
numbers = [1, 2, 3, 4]

# 1. 변환 함수 정의
def double(x): return x * 2

# 2. map() 함수 사용
mapped_iterator = map(double, numbers)

# 3. 결과를 리스트로 변환 (map()은 이터레이터를 반환하므로)
doubled_list = list(mapped_iterator) 

print(doubled_list)  # 출력: [2, 4, 6, 8]