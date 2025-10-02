def test():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")

output = test()
print("D지점 통과")
a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
c = next(output)
print(c)

next(output) # 다음 실행 대상이 없어 StopIteration이 걸린다.

# 위 제네레이터 함수는 이해를 돕기 위해 저렇게 선언됐지만
# 애초부터 Iterator를 생성할 목적의 함수이므로 yield 반복이 가능한 디자인패턴으로 선언되는게 보통이다.