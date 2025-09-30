array = [273, 32, 103, 57, 52]

# for in 구문은 리스트가 가진 요소 갯수만큼만 반복 실행
for element in array:
    print(element)

print()

for i in range(len(array)):
    print("{}번째 요소: {}".format(i, array[i]))

print() 