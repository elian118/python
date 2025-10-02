dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색"],
    "origin": "필리핀",
}

print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])

print()
print(dictionary)

dictionary["price"] = 5000
print("price:", dictionary["price"])

print()
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print()


del dictionary["ingredient"]
print(dictionary)

print()
print(dictionary.keys())
print(dictionary.values())
print()

da = [*dictionary]
dvals = [*dictionary.values()]


print("da", da) # 딕셔너리를 대상으로 전개연산자를 사용하면 키만 모아 담은 리스트가 반환된다.
print("dvals", dvals) # 딕셔너리 값만 가져오고 싶을 땐 dictionary.values() 사용



