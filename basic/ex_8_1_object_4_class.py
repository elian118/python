class Student:
    # 생성자: __init__(self, 추가적인 매개변수):
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t") # 출력물 사이마다 탭 띄우기
for student in students:
    print(student.to_string())

print()
for student in students:
    print(f"{student.name} 학생 정보의 자료형: {type(student)} | Student 인스턴스 여부: {isinstance(student, Student)}")
    