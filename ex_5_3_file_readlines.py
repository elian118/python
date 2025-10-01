with open("info.txt", "r", encoding="utf-8") as file:
    # file 객체 TextIOWrapper는 반복이 가능한 Itrable 객체다. 
    # 파이썬은 파일을 불러올 때 한 줄식 불러와 순서대로 이 객체의 데이터 요소로서 담게 되므로, 반복문으로 TextIOWrapper를 한 줄씩 읽는 게 가능하다.
    for line in file:
        (name, weight, height) = line.strip().split(", ")
        # 파일에 누락 정보가 하나라도 존재시 건너 뜀 → BMI 계산이 불가하기 때문
        if (not name) or (not weight) or (not height):
            continue
        # BMI 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)
        # 결과 판정
        result = ""
        if  25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"
        # 출력
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()
    print(type(file))