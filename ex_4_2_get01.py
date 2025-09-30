dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색"],
    "origin": "필리핀",
}

value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")

# get("key")는 단순히 값을 어떻게든 가져오는 함수다. 존재하지 않는 키로 접근 시 None을 반환한다.
# 딕셔너리는 키만 선언하고 값 자체를 비워두는 것도 가능하므로 이런 표현도 허용된다. → 오류가 아님