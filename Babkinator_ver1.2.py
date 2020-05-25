# 반복되는 질문을 통해 사용자에게 음식 메뉴를 추천
import pandas as pd         # csv 파일을 읽어오기 위해서 panda 사용

# 메뉴와 그 메뉴에 해당하는 코드를 포함하는 csv 파일 읽어오기
code_df = pd.read_csv('C:/Users/hgma1/PycharmProjects/Babkinator_ver1.2/food_code.csv')     # 파일 위치는 사용자마다 변경해주어야함

# 단계별 질문 선언
Q1 = ["고기입니까?"]
Q2 = ["얼큰한 음식입니까?", "익혀서 먹나요?"]
Q3 = ["매운 음식입니까?", "많은 양이 필요한가요?"]
Q4 = ["면요리 입니까?", "면 vs 밥", "밥이 필요한 요리입니까?", "해산물이 들어갑니까?"]
Q5 = ["밥이 필요한 요리입니까?", "닭 요리입니까?"]
Q6 = ["돼지고기가 들어갑니까?"]

# csv 파일에 미리 저장해둔 코드와 비교하기위한 변수 선언 및 질문 반복과 답변 얻기
# 고기 o/x
food_code = input(Q1[0])        # 답변을 y/n로 받아서 문자열로 변수에 저장
# 고기o
if food_code == "y":
    # 익힌 음식 o/x
    food_code += input(Q2[1])
    # 고기o, 익힌 음식o
    if food_code == "yy":
        # 매운 음식 o/x
        food_code += input(Q3[0])
        # 고기o, 익힌 음식o, 매운 음식o
        if food_code == "yyy":
            # 해산물 o/x
            food_code += input(Q4[3])
            # 고기o, 익힌 음식o, 매운 음식o, 해산물o
            if food_code == "yyyy":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
            # 고기o, 익힌 음식o, 매운 음식o, 해산물x
            elif food_code == "yyyn":
                # 닭 요리 o/x
                food_code += input(Q5[1])
                # 고기o, 익힌 음식o, 매운 음식o, 해산물x, 닭 요리 o
                if food_code == "yyyny":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
                # 고기o, 익힌 음식o, 매운 음식o, 해산물x, 닭 요리 x
                elif food_code == "yyynn":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
        # 고기o, 익힌 음식o, 매운 음식x
        elif food_code == "yyn":
            # 해산물o/x
            food_code += input(Q4[3])
            # 고기o, 익힌 음식o, 매운 음식x, 해산물o
            if food_code == "yyny":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
            # 고기o, 익힌 음식o, 매운 음식x, 해산물x
            elif food_code == "yynn":
                # 닭 요리 o/x
                food_code += input(Q5[1])
                # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리o
                if food_code == "yynny":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
                # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리x
                elif food_code == "yynnn":
                    # 돼지고기 o/x
                    food_code += input(Q6[0])
                    # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리x, 돼지 고기o
                    if food_code == "yynnny":
                        for i in range(0, len(code_df.index), 1):
                            if code_df.loc[i, '코드'] == food_code:
                                print(code_df.loc[i, '메뉴'])
                    # 고기o, 익힌 음식o, 매운 음식x, 해산물x, 닭 요리x, 돼지 고기x
                    elif food_code == "yynnnn":
                        for i in range(0, len(code_df.index), 1):
                            if code_df.loc[i, '코드'] == food_code:
                                print(code_df.loc[i, '메뉴'])
    # 고기o, 익힌 음식x
    elif food_code == "yn":
        # 양 많음 o/x
        food_code += input(Q3[1])
        # 고기o, 익힌 음식x, 양 많음o
        if food_code == "yny":
            # 밥 필요 o/x
            food_code += input(Q4[2])
            # 고기o, 익힌 음식x, 양 많음o, 밥o
            if food_code == "ynyy":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
            # 고기o, 익힌 음식x, 양 많음o, 밥x
            elif food_code == "ynyn":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
        # 고기o, 익힌 음식x, 양 많음x
        elif food_code == "ynn":
            print(food_code)
# 고기x
elif food_code == "n":
    # 얼큰한 음식o/x
    food_code += input(Q2[0])
    # 고기x, 얼큰한 음식o
    if food_code == "ny":
        # 매운 음식o/x
        food_code += input(Q3[0])
        # 고기x, 얼큰한 음식o, 매운 음식o
        if food_code == "nyy":
            # 면 vs 밥
            food_code += input(Q4[2])
            # 고기x, 얼큰한 음식o, 매운 음식o, 면o
            if food_code == "nyyy":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
            # 고기x, 얼큰한 음식o, 매운 음식o, 밥o
            elif food_code == "nyyn":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
        # 고기x, 얼큰한 음식o, 매운 음식x
        elif food_code == "nyn":
            # 면 요리o/x
            food_code += input(Q4[0])
            # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리o
            if food_code == "nyny":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
            # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리x
            elif food_code == "nynn":
                # 밥이 필요한 요리o/x
                food_code += input(Q5[0])
                # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리x, 밥 필요o
                if food_code == "nynny":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
                # 고기x, 얼큰한 음식o, 매운 음식x, 면 요리x, 밥 필요x
                elif food_code == "nynnn":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
    # 고기x, 얼큰한 음식x
    elif food_code == "nn":
        # 매운 음식o/x
        food_code += input(Q3[0])
        # 고기x, 얼큰한 음식x, 매운 음식o
        if food_code == "nny":
            # 면 요리o/x
            food_code += input(Q4[0])
            # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리o
            if food_code == "nnyy":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
            # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리x
            elif food_code == "nnyn":
                # 밥이 필요 o/x
                food_code += input(Q5[0])
                # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리x, 밥 필요o
                if food_code == "nnyny":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
                # 고기x, 얼큰한 음식x, 매운 음식o, 면 요리x, 밥 필요x
                elif food_code == "nnynn":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
        # 고기x, 얼큰한 음식x, 매운 음식x
        elif food_code == "nnn":
            # 면 요리o/x
            food_code += input(Q4[0])
            # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리o
            if food_code == "nnny":
                for i in range(0, len(code_df.index), 1):
                    if code_df.loc[i, '코드'] == food_code:
                        print(code_df.loc[i, '메뉴'])
            # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리x
            if food_code == "nnnn":
                # 밥이 필요o/x
                food_code += input(Q5[0])
                # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리x, 밥 필요o
                if food_code == "nnnny":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])
                # 고기x, 얼큰한 음식x, 매운 음식x, 면 요리x, 밥 필요x
                elif food_code == "nnnnn":
                    for i in range(0, len(code_df.index), 1):
                        if code_df.loc[i, '코드'] == food_code:
                            print(code_df.loc[i, '메뉴'])










