# 메뉴 출력
print("1. 데이터 추가\n")
print("2. 데이터 검색\n")
print("3. 데이터 삭제\n")
print("4. 데이터 정렬\n")
print("5. 전체 데이터 출력\n")              # 결과를 확인하기 위해 제가 임의로 추가했습니다!!
print("0. 종료\n")
Menu = int(input("메뉴를 선택하세요:"))     # 메뉴 선택을 위한 변수 선언

StudentDic = {}                           # 학생의 정보를 딕셔너리로 저장하기 위한 변수 선언

# 딕셔너리로 저장된 정보를 리스트로 변환하기 위한 변수 선언 및 이차원 리스트로 변환하기 위해 2개의 변수 선언
StudentList1 = []                       # 딕셔너리의 value 들을 리스트로 변환 위한 변수
StudentList2 = []                       # 2차원 리스트를 위한 변수

StudentNumber = 0                       # 저장한 학생 수

# 메뉴를 반복하기 위한 반복문
while Menu != 0:

    # 데이터 추가
    if Menu == 1:
        # 학생에 대한 정보를 딕셔너리로 저장
        StudentDic['학과'] = input("학과를 입력하세요:")
        StudentDic['학번'] = int(input("학번을 입력하세요:"))
        StudentDic['이름'] = input("이름을 입력하세요:")

        Kor = int(input("국어 성적을 입력하세요:"))
        Math = int(input("수학 성적을 입력하세요:"))
        Eng = int(input("영어 성적을 입력하세요:"))
        Sum = Kor + Math + Eng
        Avg = Sum/3.0

        if Avg >= 90:       # 학점을 위한 조건문
            Score = 'A'
        elif Avg >= 80:
            Score = 'B'
        elif Avg >= 70:
            Score = 'C'
        elif Avg >= 60:
            Score = 'D'
        else:
            Score = 'F'

        StudentDic['국어'] = Kor
        StudentDic['수학'] = Math
        StudentDic['영어'] = Eng
        StudentDic['총점'] = Sum
        StudentDic['평균'] = Avg
        StudentDic['학점'] = Score

        # 딕셔너리의 values 들을 리스트로 저장
        StudentList1 = list(StudentDic.values())
        # 리스트로 저장한 정보를 이차원리스트로 저장
        StudentList2.append(StudentList1)
        # 리스트의 길이로 학생 수 저장
        StudentNumber = len(StudentList2)

    # 데이터 검색(학번 사용)
    elif Menu == 2:
        FindID = int(input("검색하고 싶은 학생의 학번을 입력하시오:"))
        for x in range(0, StudentNumber):
            if StudentList2[x][1] == FindID:
                index = x
                print(StudentList2[index])

    # 데이터 삭제(학번 사용)
    elif Menu == 3:
        FindID = int(input("삭제하고 싶은 학생의 학번을 입력하시오:"))
        for x in range(0, StudentNumber):
            if StudentList2[x][1] == FindID:
                index = x
                del(StudentList2[index])
                break
        StudentNumber = len(StudentList2)

    # 데이터 정렬
    elif Menu == 4:
        SmallMenu = int(input("학번으로 정렬(1), 학과로 정렬(2):"))
        if SmallMenu == 1:
            StudentList2.sort(key=lambda y: y[1])
        elif SmallMenu == 2:
            StudentList2.sort(key=lambda y: y[0])

    # 전체 데이터 출력
    elif Menu == 5:
        CategoryList = ["학과", "학번", "이름", "국어", "영어", "수학", "총점", "평균", "학점"]
        print(CategoryList)
        for i in range(0, StudentNumber):
            print(StudentList2[i])

    # 메뉴를 반복적으로 제시하기 위한 출력문
    print("1. 데이터 추가\n")
    print("2. 데이터 검색\n")
    print("3. 데이터 삭제\n")
    print("4. 데이터 정렬\n")
    print("5. 전체 데이터 출력\n")
    print("0. 종료\n")
    Menu = int(input("메뉴를 선택하세요:"))

