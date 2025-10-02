# 딕셔너리 내부에 있는 특정 속성을 활용해 최소/최대값 구하기

books = [
    {
        "제목": "혼자 공부하는 파이썬",
        "가격": 18000,
    },
    {
        "제목": "혼자 공부하는 머신러닝 + 딥러닝",
        "가격": 26000,
    },
    {
        "제목": "혼자 공부하는 자바스크립트",
        "가격": 24000,
    },
]

def 가격추출함수(book):
    return book["가격"]

print("# 가장 저렴한 책 찾기")
# print(min(books, key=가격추출함수))
print(min(books, key = lambda book: book["가격"]))
print("# 가장 비싼 책 찾기")
# print(max(books, key=가격추출함수))
print(max(books, key = lambda book: book["가격"]))
