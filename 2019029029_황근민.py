# 전역변수 선언
StudentDic = {}                        # 학생의 정보를 딕셔너리로 저장하기 위한 변수 선언

StudentList = []                       # 학생 정보를 2차원 리스트로 저장하기 위한 변수

StudentNumber = 0                      # 저장한 학생 수

# 함수 선언 ==============================================================================================


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


# 데이터 저장 함수
def save_date(student_dic, student_list2):

    # 학생에 대한 정보를 딕셔너리로 저장
    student_dic['학과'] = input("학과를 입력하세요:")
    student_dic['학번'] = int(input("학번을 입력하세요:"))
    student_dic['이름'] = input("이름을 입력하세요:")

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

    student_dic['국어'] = kor
    student_dic['수학'] = math
    student_dic['영어'] = eng
    student_dic['총점'] = sum_score
    student_dic['평균'] = avg
    student_dic['학점'] = score

    # 딕셔너리의 values 들을 리스트로 저장
    student_list1 = list(student_dic.values())
    # 리스트로 저장한 정보를 이차원리스트로 저장
    student_list2.append(student_list1)
    student_number = len(student_list2)
    return student_number


# 데이터 검색 함수
def find_date(student_number, student_list):
    small_menu = int(input("학번으로 검색(1), 이름으로 검색(2):"))
    if small_menu == 1:
        find_id = int(input("검색하고 싶은 학생의 학번을 입력하시오:"))
        for i in range(0, student_number):
            if student_list[i][1] == find_id:
                find_index = i
                print(student_list[find_index])
                break

    elif small_menu == 2:
        find_name = input("검색하고 싶은 학생의 이름을 입력하시오:")
        for i in range(0, student_number):
            if student_list[i][2] == find_name:
                find_index = i
                print(student_list[find_index])
                break


# 데이터 삭제 함수
def del_date(student_number, student_list):
    small_menu = int(input("학번으로 삭제(1), 이름으로 삭제(2):"))
    if small_menu == 1:
        del_id = int(input("삭제하고 싶은 학생의 학번을 입력하시오:"))
        for i in range(0, student_number):
            if student_list[i][1] == del_id:
                del_index = i
                del (student_list[del_index])
                break

    elif small_menu == 2:
        del_name = input("삭제하고 싶은 학생의 이름을 입력하시오:")
        for i in range(0, student_number):
            if student_list[i][2] == del_name:
                del_index = i
                del (student_list[del_index])
                break

    student_number = len(student_list)
    return student_number


# 데이터 정렬 함수
def sort_date():
    small_menu = int(input("학번으로 정렬(1), 학과로 정렬(2):"))
    if small_menu == 1:
        StudentList.sort(key=lambda y: y[1])
    elif small_menu == 2:
        StudentList.sort(key=lambda y: y[0])


# 전체 데이터 출력 함수
def print_all_date(student_number, student_list):
    category_list = ["학과", "학번", "이름", "국어", "영어", "수학", "총점", "평균", "학점"]
    print(category_list)
    for i in range(0, student_number):
        print(student_list[i])

# =====================================================================================================


# 메뉴 출력
Menu = print_menu()


# 메뉴를 반복하기 위한 반복문
while Menu != 0:

    # 데이터 추가
    if Menu == 1:
        StudentNumber = save_date(StudentDic, StudentList)

    # 데이터 검색
    elif Menu == 2:
        find_date(StudentNumber, StudentList)

    # 데이터 삭제
    elif Menu == 3:
        StudentNumber = del_date(StudentNumber, StudentList)

    # 데이터 정렬
    elif Menu == 4:
        sort_date()

    # 전체 데이터 출력
    elif Menu == 5:
        print_all_date(StudentNumber, StudentList)

    # 메뉴를 반복적으로 제시
    Menu = print_menu()

