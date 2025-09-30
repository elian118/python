list_a = [1, 2, 3]

print('# 리스트 뒤에 요소 추가하기')
list_a.append(4)
list_a.append(5)

print(list_a)

print('# 리스트 중간에 요소 추가하기')
list_a.insert(3, 10)
print(list_a)

# append(), insert(), extend(), del(), pop(), remove(), clear() 등의 함수를 원본에 영향을 주는 '파괴적 연산'이라고도 표현한다.