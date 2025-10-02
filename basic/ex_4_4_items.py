example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

print("# 딕셔너리 items() 함수")
print("items:", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수 조합해서 사용하기")
for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
print()