try:
    file = open("info.txt", "w")
    예외.발생해라
except:
    print("오류가 발생했습니다.")
finally:
    file.close()

# file.close() # finally 대신 이렇게 해도 문제 없다.
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 꼭 finally로 file.close() 할 필요는 없다.
# 단지, finally사용하면 try 코드와의 연관성이 더욱 잘 보이기 때문.
# 그리고 finally는 이런 간단한 경우보단, 
# try 구문 내부에서 return 키워드를 사용하거나 반복문과 함께 사용할 때처럼
# 코드 실행 도중에 끝날 가능성이 높은 코드에서 사용했을 때 더 깔끔해보인다.