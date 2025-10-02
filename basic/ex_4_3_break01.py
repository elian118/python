numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    print(number)

print()

numbers = [1, 15, 8, 22, 5, 30]

# 리스트 컴프리헨션 사용 (더 간결함)
filtered_list = [number for number in numbers if number > 10]
filtered_list2 = [number * 2 for number in numbers if number > 10]

print(filtered_list)  # 출력: [15, 22, 30]
print(filtered_list2)  # 출력: [30, 44, 60]

# 사용법: [결과표현식 for 루프변수 in 리스트 if 조건식]

# 그 외 언패킹이라는 구조분해와 유사한 문법이 있다.
data = ["Alice", 25, "New York", "Engineer", 5000]

# name과 age만 할당하고, 나머지는 모두 'details' 리스트에 모음
name, age, *details = data # 언패킹과 전개 연산자 조합

print(name)     # 출력: Alice
print(age)      # 출력: 25
print(details)  # 출력: ['New York', 'Engineer', 5000]