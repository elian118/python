array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

print()
# 리스트 내포 문법: [결과 표현식 for 루프변수 in 리스트 또는 범위]
array = [i * i for i in range(0, 20, 2)]
print(array)

print()

# 필터링 기법인 리스트 컴프레션과 사용법이 유사하다.

array = [i * i for i in range(0, 20, 2) if i > 10] # 리스트 컴프레션은 여기에 조건식이 추가된다.
print(array)