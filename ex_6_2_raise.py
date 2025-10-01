number = input("정수 입력> ")
number = int(number)

if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError

# try except 구문과 별개로 오류를 강제로 발생시키는 raise [예외 객체] 구문도 있다.
# 주로, 개발자의 실수를 막기 위해 오류로 경각심을 일깨우고자 이런 키워드가 사용된다.