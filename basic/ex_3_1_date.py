import datetime

now = datetime.datetime.now()

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

(year, month, day, hour, minute, second, *rest) = datetime.datetime.now().timetuple() # 가끔 파이썬에선 편의를 위해 전개 연산자로 추출 가능한 튜플 자료형을 제공하는 경우가 있다.

print("{}년 {}월 {}일 {}시 {}분 {}초".format(year, month, day, hour, minute, second))
print(rest)