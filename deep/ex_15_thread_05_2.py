# 락 객체를 사용한 동기화 처리

import threading

Q = 100000  # 스레드 공유 데이터 - 대기열 수
thread_list = []
mylock = threading.Lock()

def drink(max):
    global Q
    for i in range(0, max):
        mylock.acquire()    #  잠금 - 스레딩 상태일때 다른 스레드가 접근할 수 없도록
        Q -= 1
        print(f"남은 대기열 수: {Q}")
        mylock.release()    # 잠금 해제

# 스레드 두개 설정
for i in range(0, 2):
    thread_inst = threading.Thread(target = drink, args = (50000, ))
    thread_list.append(thread_inst)
    thread_inst.start()

for thread in thread_list:
    thread.join()

print(Q)

# 스레드 Lock 객체를 활용하면 acquire(), release() 함수를 사용해 스레드 간 경합 문제를 해결할 수 있다.