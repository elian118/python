# 간단한 동기화 처리 예제

import threading

Q = 100000          # 스레드 공유 데이터 - 대기열 수
thread_list = []    # 스레드 리스트

def drink(max):
    global Q
    for i in range(0, max):
        Q -= 1
        print(f"남은 대기열 수: {Q}")

# 스레드 두개 설정
for i in range(0, 2):
    thread_inst = threading.Thread(target = drink, args = (50000, ))
    thread_list.append(thread_inst) # 생성된 스레드를 스레드 목록에 저장
    thread_inst.start() # 스레드 실행

for thread in thread_list:
    thread.join()   # 앞 스레드가 종료될 때까지 대기(실행중인 스레드 종료)

print(Q)

# 위 예제는 스레드 두개가 공유데이터를 다룰 때 경합할 수 있는 문제를 해결하는 방법의 개념을 설명한다.