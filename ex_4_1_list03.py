list_a = [0, 1, 2, 3, 4, 5]
del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2) # 인자 생략 시 -1 입력으로 간주 → 가장 마지막 요소 제거
print("pop(2):", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print("del list_b[3:6]:", list_b)

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print("del list_c[:3]:", list_c)