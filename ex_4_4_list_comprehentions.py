array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# [결과 표현식 for 루프변수 in 리스트 또는 범위 if 조건식]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)

print()