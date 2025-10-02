# 재귀함수로 모든 리스트 요소들을 1차원 수준으로 평탄화하는 예제 → 디버거를 쓰면 어찌 돌아가는지 확인 가능
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item) # 요소가 리스트 형이면 재귀 호출해 반환 → else문이 실행되며 리스트 안의 요소가 꺼내져 부모 리스트에 편입
        else:
            output.append(item) # 그 외 요소는 그냥 담는다
    return output # 반환

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))

# 평탄화 함수는 워낙 많이 쓰이고 있고, 이미 여러 파이썬 라이브러리에서 제공되고 있다.

# 1. itertools 사용
# import itertools

# nested_list = [[1, 2], [3, 4, 5], [6]]


# flattened_list = list(itertools.chain.from_iterable(nested_list))

# 2. numpy 사용
# import numpy as np

# nested_array = np.array([[1, 2], [3, 4]])

# # 배열의 모든 차원을 1차원으로 평탄화합니다.
# flattened_array = nested_array.flatten()
