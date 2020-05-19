# csv 파일을 읽어와 검색하여 원하는 식당이 있으면 지도에 그 식당을 표시
import folium               # folium: 지도를 위한 모듈
import pandas as pd         # pandas: csv 파일을 읽어오기 위한 모듈


class RestaurantMarker:

    def __init__(self):
        self.center = [36.629049, 127.456318]                                       # 충북대학교 솔못 좌표
        self.map = folium.Map(location=self.center, zoom_start=15)                  # 충북대학교를 기준으로 지도데이터 생성
        self.df = pd                                                                # csv 파일을 판다스를 통해 읽어올 변수
        self.find_restaurant = ''                                                   # 찾을 식당의 변수 선언

    # 판다스를 통해 csv 파일을 읽어옴
    def open_csv(self):
        self.df = pd.read_csv('C:/Users/hgma1/PycharmProjects/기초프로젝트/restaurant_list.csv', encoding='CP949')
        # <C:/Users/hgma1/PycharmProjects/기초프로젝트> 부분은 파일의 위치(경로) 부분이므로 개발자마다 위치가 달라 수정해야함
        # encoding='CP949' csv 파일을 판다스를 통해 읽어 올 때 생기는 오류를 위한 코드

    # 식당을 판다스를 통해 csv 파일 기준으로 검색 후 지도에 표시
    def restaurant_marker(self):
        self.find_restaurant = input("지도에 표시할 업소명:")
        for i in range(0, len(self.df.index), 1):
            if self.df.loc[i]['업소명'] == self.find_restaurant:           # 검색
                folium.Marker(                                            # 표시
                    location=self.df.loc[i, ['위도', '경도']],            # csv 파일 기준
                    tooltip=self.df.loc[i]['업소명'],                    # csv 파일 기준
                ).add_to(self.map)
                break

    # 충북대학교의 위치를 지도에 표시
    def center_marker(self):
        folium.Marker(
            location=[36.629049, 127.456318],
            tooltip='충북대학교'
        ).add_to(self.map)

    # 충북대학교와 검색한 식당을 표시한 지도 html로 저장
    def save_html(self):
        self.map.save('restaurant_marked_map.html')


Restaurant = RestaurantMarker()

Restaurant.open_csv()
Restaurant.restaurant_marker()
Restaurant.center_marker()
Restaurant.save_html()


# 원래 코드
"""

df = pd.read_csv('C:/Users/hgma1/PycharmProjects/기초프로젝트/restaurant_list.csv', encoding='CP949')

# 충북대학교 좌표를 변수에 지정 및 지도에서 중심으로 표현
center = [36.629049, 127.456318]
m = folium.Map(location=center, zoom_start=15)

find_restaurant = input("지도에 표시할 업소명:")

for i in range(0, len(df.index), 1):
    if df.loc[i]['업소명'] == find_restaurant:
        folium.Marker(
            location=df.loc[i, ['위도', '경도']],
            tooltip=df.loc[i]['업소명'],
        ).add_to(m)
        break


folium.Marker(
    location=[36.629049, 127.456318],
    tooltip='충북대학교'
).add_to(m)

m.save('index.html')
"""
