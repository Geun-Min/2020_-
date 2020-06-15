import pandas as pd


class Management_csv():

    def __init__(self):
        self.foodcode_df = pd
        self.restarurant_df = pd
        self.food_code = ""
        self.food_name = ""
        self.code_list = []

    # 식당 정보 csv 파일 읽기
    def open_restaurnat_csv(self):
        self.restarurant_df = pd.read_csv('./res_data.csv', encoding='CP949')

    def open_foodcode_csv(self):
        self.foodcode_df = pd.read_csv('./food_code.csv', encoding='utf-8-sig')
        print(self.foodcode_df)

    def babkinator(self):
        q0 = ["고기입니까?(해산물 포함)"]
        q1 = ["익힌 음식입니까?", "매운 음식입니까?"]
        q2 = ["매운 음식입니까?", "해산물이 들어가는 음식입니까?", "면이 들어가는 음식입니까?"]
        q3 = ["해산물이 들어가는 음식입니까?", "밥이 들어가거나 밥과 함께 먹는 음식입니까?"]
        q4 = ["탕요리입니까?", "닭이 들어가는 음식입니까?"]
        q5 = ["찜요리입니까?", "돼지고기가 들어가는 음식입니까?"]
        q6 = ["조림 요리입니까?", "튀긴 음식입니까?"]
        q7 = ["볶음요리입니까?"]

        # 0단계 질문
        if len(self.food_code) == 0:
            # 고기입니까?
            self.food_code = input(q0[0])

        while self.food_code != "":

            # 1단계 질문
            if len(self.food_code) == 1:

                # 고기o
                if self.food_code == "y":
                    # 익힌 음식입니까?
                    self.food_code += input(q1[0])

                # 고기x
                elif self.food_code == "n":
                    # 매운 음식입니까?
                    self.food_code += input(q1[1])

            # 2단계 질문
            elif len(self.food_code) == 2:

                # 고기o, 익힘o
                if self.food_code == "yy":
                    # 매운 음식입니까?
                    self.food_code += input(q2[0])

                # 고기o, 익힘x
                elif self.food_code == "yn":
                    # 해산물이 들어가는 음식입니까?
                    self.food_code += input(q2[1])

                # 고기x, 매움o 또는 고기x, 매움x
                elif (self.food_code == "ny") or (self.food_code == "nn"):
                    # 면이 들어가는 음식입니까?
                    self.food_code += input(q2[2])

            # 3단계 질문
            elif len(self.food_code) == 3:

                # 고기o, 익힘o, 매움o 또는 고기o, 익힘o, 매움x
                if (self.food_code == "yyy") or (self.food_code == "yyn"):
                    # 해산물이 들어가는 음식입니까?
                    self.food_code += input(q3[0])

                # 고기o, 익힘x, 해산물o 또는 고기x, 매움o, 면x 또는 고기x, 매움x, 면x
                elif (self.food_code == "yny") or (self.food_code == "nyn") or (self.food_code == "nnn"):
                    # 쌀이 들어가거나 밥과 함께 먹는 음식입니까?
                    self.food_code += input(q3[1])

                # 고기o, 익힘x, 해산물x 또는 고기x, 매움o, 면o 또는 고기x, 매움x, 면o
                elif (self.food_code == "ynn") or (self.food_code == "nyy") or (self.food_code == "nny"):
                    return self.food_code

            # 4단계 질문
            elif len(self.food_code) == 4:

                # 고기o, 익힘o, 매움o, 해산물o
                if self.food_code == "yyyy":
                    self.food_code += input(q4[0])

                # 고기o, 익힘o, 매움x, 해산물o 또는
                # 고기o, 익힘x, 해산물o, 쌀o 또는 고기o, 익힘x, 해산물o, 쌀x 또는
                # 고기x, 매움o, 면x, 쌀o 또는 고기x, 매움o, 면x, 쌀x 또는
                # 고기x, 매움x, 면x, 쌀o 또는 고기x, 매움x, 면x, 쌀x
                
                elif (self.food_code == "yyny") or \
                     (self.food_code == "ynyy") or (self.food_code == "ynyn") or \
                     (self.food_code == "nyny") or (self.food_code == "nynn") or \
                     (self.food_code == "nnny") or (self.food_code == "nnnn"):
                    return self.food_code

                # 고기o, 익힘o, 매움o, 해산물x 또는 고기o, 익힘o, 매움x, 해산물x
                elif (self.food_code == "yyyn") or (self.food_code == "yynn"):
                    # 닭이 들어가는 음식입니까?
                    self.food_code += input(q4[0])

            # 5단계 질문
            elif len(self.food_code) == 5:

                """
                    고기o, 익힘o, 매움o, 해산물x, 닭o 또는 고기o, 익힘o, 매움o, 해산물x, 닭x 또는
                    고기o, 익힘o, 매움x, 해산물x, 닭o
                """
                if (self.food_code == "yyyny") or (self.food_code == "yyynn") or \
                   (self.food_code == "yynny"):
                    return self.food_code

                # 고기o, 익힘o, 매움x, 해산물x, 닭x
                elif self.food_code == "yynnn":
                    # 돼지고기가 들어가는 음식입니까?
                    self.food_code += input(q5[0])

            # 6단계 질문
            elif len(self.food_code) == 6:

                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지o
                if self.food_code == "yynnny":
                    self.food_code += input(q6[0])

                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지x
                elif self.food_code == "yynnnn":
                    return self.food_code

            # 7단계
            elif len(self.food_code) == 7:

                # 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지o, 튀김o 또는 고기o, 익힘o, 매움x, 해산물x, 닭x, 돼지o, 튀김x
                if (self.food_code == "yynnnyy") or (self.food_code == "yynnnyn"):
                    return self.food_code

    # 음식 코드 csv 파일에서 메뉴에 대한 코드를 수정하는 함수
    def modfiy_foodcode(self, code_list):

        self.foodcode_df.loc[code_list[0], '메뉴'] = code_list[1]
        self.foodcode_df.loc[code_list[0], '코드'] = code_list[2]

        self.foodcode_df.to_csv('food_code.csv',  encoding='utf-8-sig', mode='w', index=False)

    # 음식 코드 csv 파일에 메뉴와 코드를 추가하는 함수
    def add_foodcode(self, food_name, code):
        index = len(self.foodcode_df.index) + 1

        self.foodcode_df.loc[index, '메뉴'] = food_name
        self.foodcode_df.loc[index, '코드'] = code

        self.foodcode_df.to_csv('food_code.csv', encoding='utf-8-sig', mode='w', index=False)

    def search_foodcode(self):
        self.food_name = input("수정할 음식을 입력하세요:")

        for i in range(0, len(self.foodcode_df.index), 1):
            if self.foodcode_df.loc[i, '메뉴'] == self.food_name:
                self.code_list = [i, self.foodcode_df.loc[i, '메뉴'], self.foodcode_df.loc[i, '코드']]
                break

        print(self.code_list)
        return self.code_list


def print_menu():
    print("1. 식당 csv 파일 관리\n")
    print("2. 음식 code csv 파일 관리\n")
    print("0. 종료\n")
    menu = int(input("메뉴를 선택하세요:"))
    return menu


Manage_csv = Management_csv()
code_list = []

# 메뉴 출력
Menu = print_menu()

while Menu != 0:
    code = ""

    # 식당 csv 파일 관리
    if Menu == 1:
        print("더미\n")

    # 음식 code csv 파일 관리
    elif Menu == 2:
        Manage_csv.open_foodcode_csv()
        print("1. 데이터 수정\n")
        print("2. 데이터 추가\n")
        small_menu = int(input("메뉴를 선택하세요:"))

        if small_menu == 1:

            # 수정할 음식 메뉴 검색
            code_list = Manage_csv.search_foodcode()

            # 밥키네이터 통해서 code 입력
            code_list[2] = Manage_csv.babkinator()

            # 수정할 음식과 토드 확인
            print(code_list)

            # 수정한 음식 메뉴와 해당 코드 csv 파일에 저장
            Manage_csv.modfiy_foodcode(code_list)
            break

        elif small_menu == 2:

            # 추가할 음식 입력
            Food_Name = input("추가할 음식을 입력하세요:")

            # 밥키네이터 통해서 code 입력
            Code = Manage_csv.babkinator()

            # 추가할 음식과 코드 확인
            print(Food_Name, Code)

            # 음식메뉴와 해당 코드 csv 파일에 저장
            Manage_csv.add_foodcode(Food_Name, Code)
            break


