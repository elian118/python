from urllib import request

target = request.urlopen("http://google.co.kr")
output = target.read()

print(output)