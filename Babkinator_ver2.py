# 2019029029 황근민
# 반복되는 질문을 통해 사용자에게 음식 메뉴를 추천
import pandas as pd         # csv 파일을 읽어오기 위해서 pandas 사용


class Bapkinator:

    # 변수 선언
    def __init__(self):
        self.restaurant_df = pd                  # 식당 정보 csv 파일을 읽어와 저장할 변수
        self.code_df = pd                       # 음식 메뉴 코드 csv 파일을 읽어와 저장할 변수
        self.food_code = ""                     # 반복되는 질문에 답변을 코드형태로 저장할 변수
        self.chosen_food_list = []              # 질문에 답변에 대해 해당하는 메뉴를 저장할 리스트

    # pandas를 이용해 csv 파일을 읽어 저장
    # 경로 부분은 개발자마다 수정이 필요
    def open_csv(self):
        # 식당 정보 csv
        self.restaurant_df = pd.read_csv('C:/Users/hgma1/PycharmProjects/Babkinator_ver2/restaurant_list1.csv', encoding='CP949')
        # 음식 메뉴 코드 csv
        self.code_df = pd.read_csv('C:/Users/hgma1/PycharmProjects/Babkinator_ver2/food_code.csv', encoding='UTF8')

    # 반복되는 질문을 통해 사용자에게 음식 메뉴 추천
    def bapkinator(self):

        # 단계별 질문 선언
        Q1 = ["고기입니까?"]
        Q2 = ["얼큰한 음식입니까?", "익혀서 먹나요?"]
        Q3 = ["매운 음식입니까?", "많은 양이 필요한가요?"]
        Q4 = ["면요리 입니까?", "면 vs 밥", "밥이 필요한 요리입니까?", "해산물이 들어갑니까?"]
        Q5 = ["밥이 필요한 요리입니까?", "닭 요리입니까?"]
        Q6 = ["돼지고기가 들어갑니까?"]

        self.food_code = input(Q1[0])  # 답변을 y/n로 받아서 문자열로 변수에 저장
        # 고기o
        if self.food_code == "y":
            # 익힌 음식 o/x
            self.food_code += input(Q2[1])
            # 고기o, 익힌 음식o
            if self.food_code == "yy":
                # 매운 음식 o/x
                self.food_code += input(Q3[0])
                # 고기o, 익힌 음식o, 매운 음식o
                if self.food_code == "yyy":
                    # 해산물 o/x
                    self.food_code += input(Q4[3])
                    # 고기o, 익힌 음식o, 매운 음식o, 해산물o
                    if self.food_code == "yyyy":
                        return self.food_code
                    # 고기o, 익힌 음식o, 매운 음식o, 해산물x
                    elif self.food_code == "yyyn":
                        # 닭 요리 o/x
                        self.food_code += input(Q5[1])
                        # 고기o, 익힌 음식o, 매운 음식o, 해산물x, 닭 요리 o
                        if self.food_code == "yyyny":
                            return self.food_code
                        # 고기o, 익힌 음식o, 매운 음식o, 해산물x, 닭 요리 x
                        elif self.food_code == "yyynn":
                            return self.food_code
                # 고기o, 익힌 음식o, 매운 음식x
                elif self.food_code == "yyn":
                    # 해산물o/x
                    self.food_code += input(Q4[3])
                    # 고기o, 익힌 음식o, 매운 음식x, 해산물o
                    if self.food_code == "yyny":
                        return self.food_code
                    # 고기o, 익힌 음식o, 매운 음식x, 해산물x
                    elif self.food_code == "yynn":
                        # 닭 요리 o/x
                        self.food_code += input(Q5[1])
                        # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리o
                        if self.food_code == "yynny":
                            return self.food_code
                        # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리x
                        elif self.food_code == "yynnn":
                            # 돼지고기 o/x
                            self.food_code += input(Q6[0])
                            # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리x, 돼지 고기o
                            if self.food_code == "yynnny":
                                return self.food_code
                            # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리x, 돼지 고기x
                            elif self.food_code == "yynnnn":
                                return self.food_code
            # 고기o, 익힌 음식x
            elif self.food_code == "yn":
                # 양 많음 o/x
                self.food_code += input(Q3[1])
                # 고기o, 익힌 음식x, 양 많음o
                if self.food_code == "yny":
                    # 밥 필요 o/x
                    self.food_code += input(Q4[2])
                    # 고기o, 익힌 음식x, 양 많음o, 밥o
                    if self.food_code == "ynyy":
                        return self.food_code
                    # 고기o, 익힌 음식x, 양 많음o, 밥x
                    elif self.food_code == "ynyn":
                        return self.food_code
                # 고기o, 익힌 음식x, 양 많음x
                elif self.food_code == "ynn":
                    return self.food_code
        # 고기x
        elif self.food_code == "n":
            # 얼큰한 음식o/x
            self.food_code += input(Q2[0])
            # 고기x, 얼큰한 음식o
            if self.food_code == "ny":
                # 매운 음식o/x
                self.food_code += input(Q3[0])
                # 고기x, 얼큰한 음식o, 매운 음식o
                if self.food_code == "nyy":
                    # 면 vs 밥
                    self.food_code += input(Q4[1])
                    # 고기x, 얼큰한 음식o, 매운 음식o, 면o
                    if self.food_code == "nyyy":
                        return self.food_code
                    # 고기x, 얼큰한 음식o, 매운 음식o, 밥o
                    elif self.food_code == "nyyn":
                        return self.food_code
                # 고기x, 얼큰한 음식o, 매운 음식x
                elif self.food_code == "nyn":
                    # 면 요리o/x
                    self.food_code += input(Q4[0])
                    # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리o
                    if self.food_code == "nyny":
                        return self.food_code
                    # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리x
                    elif self.food_code == "nynn":
                        # 밥이 필요한 요리o/x
                        self.food_code += input(Q5[0])
                        # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리x, 밥 필요o
                        if self.food_code == "nynny":
                            return self.food_code
                        # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리x, 밥 필요x
                        elif self.food_code == "nynnn":
                            return self.food_code
            # 고기x, 얼큰한 음식x
            elif self.food_code == "nn":
                # 매운 음식o/x
                self.food_code += input(Q3[0])
                # 고기x, 얼큰한 음식x, 매운 음식o
                if self.food_code == "nny":
                    # 면 요리o/x
                    self.food_code += input(Q4[0])
                    # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리o
                    if self.food_code == "nnyy":
                        return self.food_code
                    # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리x
                    elif self.food_code == "nnyn":
                        # 밥이 필요 o/x
                        self.food_code += input(Q5[0])
                        # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리x, 밥 필요o
                        if self.food_code == "nnyny":
                            return self.food_code
                        # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리x, 밥 필요x
                        elif self.food_code == "nnynn":
                            return self.food_code
                # 고기x, 얼큰한 음식x, 매운 음식x
                elif self.food_code == "nnn":
                    # 면 요리o/x
                    self.food_code += input(Q4[0])
                    # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리o
                    if self.food_code == "nnny":
                        return self.food_code
                    # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리x
                    if self.food_code == "nnnn":
                        # 밥이 필요o/x
                        self.food_code += input(Q5[0])
                        # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리x, 밥 필요o
                        if self.food_code == "nnnny":
                            return self.food_code
                        # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리x, 밥 필요x
                        elif self.food_code == "nnnnn":
                            return self.food_code

    # 질문 통해 받은 결과와 음식 메뉴 코드 csv 비교 통해 해당하는 음식 메뉴 리스트 변수에 음식 메뉴 저장
    def make_food_list(self):
        for i in range(0, len(self.code_df.index), 1):
            if self.code_df.loc[i, '코드'] == self.food_code:
                self.chosen_food_list.append(self.code_df.loc[i, '메뉴'])
        print(self.chosen_food_list)
        return self.chosen_food_list

    # 사용자가 선택한 음식 메뉴에 해당하는 식당 정보 출력
    def print_restaurant_information(self):
        list_index = int(input("어떤 메뉴의 식당 정보를 원하세요?(1 ~ %d):" % len(self.chosen_food_list)))
        for i in range(0, len(self.restaurant_df.index), 1):
            if self.restaurant_df.loc[i, '메뉴'] == self.chosen_food_list[list_index - 1]:
                print(self.restaurant_df.loc[i, '업소명'])
                print(self.restaurant_df.loc[i, '주소'])
                print(self.restaurant_df.loc[i, '전화번호'])
                print(self.restaurant_df.loc[i, '웹페이지'])
                print(self.restaurant_df.loc[i, '가격대'])
                print(self.restaurant_df.loc[i, '메뉴'])
                print("======================================")


# 실행 예시
sample = Bapkinator()
sample.open_csv()
sample.bapkinator()
sample.make_food_list()

y_n = input("식당 정보를 원하세요?(y/n)")
if y_n == "y":
    print("\n")
    sample.print_restaurant_information()

