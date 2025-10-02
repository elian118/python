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

print("# 가격 오름차순 정렬")
# sort() 역시 원본을 변형하는 파괴적 함수다. 원본 파괴를 원치 않는다면 전개연산자를 활용하자
copyBooks = [*books]
copyBooks.sort(key = lambda book: book["가격"])
for book in copyBooks:
    print(book)
print()

print("# 가격 내림차순 정렬")
copyBooks = [*books]
copyBooks.sort(reverse = True, key = lambda book: book["가격"])
for book in copyBooks:
    print(book)
print()

print("# 원본 출력")
for book in books:
    print(book)
print()