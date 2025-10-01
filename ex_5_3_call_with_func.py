def power(item): return item * item

def under_3(item): return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a):", output_a)        # map() → object 자료형으로 반환하므로, 즉시 확인 불가 
print("map(power, list_input_a):", list(output_a))  # list 자료형으로 형변환 후 확인 가능
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a):", output_b)       # filter() → object 자료형으로 반환하므로, 즉시 확인 불가 
print("filter(under_3, list_input_a):", list(output_b)) # list 자료형으로 형변환 후 확인 가능
print()