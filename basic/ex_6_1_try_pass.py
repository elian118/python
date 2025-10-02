list_input = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input:
    try:
        float(item)
        list_number.append(item)
    except:
        pass # 이렇게 하면 오류 발생 시 무시하고 continue

print("{} 내부에 있는 숫자는".format(list_input))
print("{}입니다.".format(list_number))
print()