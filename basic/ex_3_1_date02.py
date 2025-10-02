import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시 {}분으로 오전입니다!".format(now.hour, now.minute))
if now.hour >= 12:
    print("현재 시각은 {}시 {}분으로 오후입니다".format(now.hour, now.minute))