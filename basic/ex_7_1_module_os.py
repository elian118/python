# os 모듈은 운영체제 명령을 파이썬 코드 안에서 실행할 수 있도록 지원한다.

import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())
print()

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")

os.rename("original.txt", "new.txt")

os.remove("new.txt")

os.system("dir")