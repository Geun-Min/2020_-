# 2019029029 황근민
# 반복되는 질문을 통해 얻은 답변으로 사용자에게 음식 메뉴를 추천
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
        self.restaurant_df = pd.read_csv('./restaurant_list1.csv', encoding='CP949')
        # 음식 메뉴 코드 csv
        self.code_df = pd.read_csv('./food_code.csv', encoding='UTF8')

    # 질문 통해 받은 결과를 외부에서 받아와 음식 메뉴 코드 csv 비교 통해 해당하는 음식 메뉴 리스트 변수에 음식 메뉴 저장
    def make_food_list(self, food_code):
        for i in range(0, len(self.code_df.index), 1):
            if self.code_df.loc[i, '코드'] == food_code:
                self.chosen_food_list.append(self.code_df.loc[i, '메뉴'])
        print(self.chosen_food_list)
        return self.chosen_food_list


# 실행 예시
sample = Bapkinator()
sample.open_csv()
sample.make_food_list("nnynn")


