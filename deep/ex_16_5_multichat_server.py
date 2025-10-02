from socket import *
import threading

sevsock = socket(AF_INET, SOCK_STREAM)
sevsock.bind(('127.0.0.1', 62580))
sevsock.listen()
print("Start Chat - Server")
print("Waiting for connection...\n")

cli_list = []   # 접속한 클라이언트 목록
cli_ids = []    # 접속한 클라이언트 아이디 목록

def receive(clisock):
    global cli_list
    while True:
        try:
            data = clisock.recv(1024)
        # 비정상 종료
        except ConnectionError: 
            print("{}와의 연결이 끊겼습니다. # code1".format(clisock.fileno()))
            break

        # 정상 종료
        if not data:    
            print("{}이 연결 종료 요청을 합니다. # code0".format(clisock.fileno()))
            clisock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break
        
        data_with_ID = bytes(str(clisock.fileno()), 'utf-8') + b":" + data
        for sock in cli_list:
            if sock != clisock:
                sock.send(data_with_ID) # 전체 클라이언트에게 메시지 전송

    cli_ids.remove(clisock.fileno())
    cli_list.remove(clisock)
    print(f"현재 연결된 사용자: {cli_ids}\n", end = '') ###
    clisock.close()

    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print("#-----------------------------------#")
    return 0

def connection():
    global cli_list
    global cli_ids
    while True:
        clisock, cliaddr = sevsock.accept()
        cli_list.append(clisock)
        cli_ids.append(clisock.fileno())
        print(f"{clisock.fileno()}가 접속하였습니다.")
        print(f"{cliaddr}가 접속하였습니다.")
        print(f"현재 연결된 사용자 {cli_ids}\n.") ###
        # 스레드 생성
        thread_recv = threading.Thread(target = receive, args=(clisock,))
        thread_recv.start()

# 스레드 생성
thread_connection = threading.Thread(target = connection, args = ())
thread_connection.start()

###### 채팅서버 서비스 중 #######

thread_connection.join()
sevsock.close()
        