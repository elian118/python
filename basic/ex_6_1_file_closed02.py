try:
    file = open("info.txt", "w")
    예외.발생해라()
    file.close()
except:
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# try-except 구문이 만능은 아니다. file.close() 도달 전에 이미 예외가 발생하면 프로그램 종료만 막을 뿐, 그 이후 코드인 열린 파일을 닫는 처리를 못한 걸 확인할 수 있다.
# 이 경우, finally 구문을 사용해 처리하면 가능하다.