# 성적관리프로그램 ver.객체지향


class ScoreManagement:
    # 인스턴스 변수 선언
    student_dic = {}  # 학생의 정보를 딕셔너리로 저장하기 위한 변수 선언

    student_list2 = []  # 학생 정보를 2차원 리스트로 저장하기 위한 변수

    student_number = 0  # 저장한 학생 수

    # 클래스 변수 선언
    category_list = ["학과", "학번", "이름", "국어", "영어", "수학", "총점", "평균", "학점"]

    def __init__(self):
        self.student_number = 0
        self.student_dic = {}
        self.student_list1 = []
        self.student_list2 = []
        self.small_menu = 0

    def save_data(self):
        # 학생에 대한 정보를 딕셔너리로 저장
        self.student_dic['학과'] = input("학과를 입력하세요:")
        self.student_dic['학번'] = int(input("학번을 입력하세요:"))
        self.student_dic['이름'] = input("이름을 입력하세요:")

        kor = int(input("국어 성적을 입력하세요:"))
        math = int(input("수학 성적을 입력하세요:"))
        eng = int(input("영어 성적을 입력하세요:"))
        sum_score = kor + math + eng
        avg = sum_score / 3.0

        if avg >= 90:  # 학점을 위한 조건문
            score = 'A'
        elif avg >= 80:
            score = 'B'
        elif avg >= 70:
            score = 'C'
        elif avg >= 60:
            score = 'D'
        else:
            score = 'F'

        self.student_dic['국어'] = kor
        self.student_dic['수학'] = math
        self.student_dic['영어'] = eng
        self.student_dic['총점'] = sum_score
        self.student_dic['평균'] = avg
        self.student_dic['학점'] = score

        # 딕셔너리의 values 들을 리스트로 저장
        self.student_list1 = list(self.student_dic.values())
        # 리스트로 저장한 정보를 이차원리스트로 저장
        self.student_list2.append(self.student_list1)
        self.student_number = len(self.student_list2)
        return self.student_number

    def find_data(self):
        self.small_menu = int(input("학번으로 검색(1), 이름으로 검색(2):"))
        if self.small_menu == 1:
            find_id = int(input("검색하고 싶은 학생의 학번을 입력하시오:"))
            for i in range(0, self.student_number):
                if self.student_list2[i][1] == find_id:
                    find_index = i
                    print(self.student_list2[find_index])
                    break

        elif self.small_menu == 2:
            find_name = input("검색하고 싶은 학생의 이름을 입력하시오:")
            for i in range(0, self.student_number):
                if self.student_list2[i][2] == find_name:
                    find_index = i
                    print(self.student_list2[find_index])
                    break

    def del_data(self):
        self.small_menu = int(input("학번으로 삭제(1), 이름으로 삭제(2):"))
        if self.small_menu == 1:
            del_id = int(input("삭제하고 싶은 학생의 학번을 입력하시오:"))
            for i in range(0, self.student_number):
                if self.student_list2[i][1] == del_id:
                    del_index = i
                    del (self.student_list2[del_index])
                    break

        elif self.small_menu == 2:
            del_name = input("삭제하고 싶은 학생의 이름을 입력하시오:")
            for i in range(0, self.student_number):
                if self.student_list2[i][1] == del_name:
                    del_index = i
                    del (self.student_list2[del_index])
                    break

        student_number = len(self.student_list2)
        return student_number

    def sort_date(self):
        self.small_menu = int(input("학번으로 정렬(1), 학과로 정렬(2):"))
        if self.small_menu == 1:
            self.student_list2.sort(key=lambda y: y[1])
        elif self.small_menu == 2:
            self.student_list2.sort(key=lambda y: y[0])

    def print_all_date(self):
        print(ScoreManagement.category_list)
        for i in range(0, self.student_number):
            print(self.student_list2[i])


# 메뉴 출력 함수
def print_menu():
    print("1. 데이터 추가\n")
    print("2. 데이터 검색\n")
    print("3. 데이터 삭제\n")
    print("4. 데이터 정렬\n")
    print("5. 전체 데이터 출력\n")              # 결과를 확인하기 위해 제가 임의로 추가했습니다!!
    print("0. 종료\n")
    menu = int(input("메뉴를 선택하세요:"))     # 메뉴 선택을 위한 변수 선언
    return menu


StudentGroup1 = ScoreManagement()
StudentGroup1.student_number = 0

# 메뉴 출력
Menu = print_menu()

while Menu != 0:

    # 데이터 추가
    if Menu == 1:
        StudentGroup1.student_number = StudentGroup1.save_data()

    elif Menu == 2:
        StudentGroup1.find_data()

    elif Menu == 3:
        StudentGroup1.student_number = StudentGroup1. del_data()

    elif Menu == 4:
        StudentGroup1.sort_date()

    elif Menu == 5:
        StudentGroup1.print_all_date()

    Menu = print_menu()
