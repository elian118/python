from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250925.xml")

soup = BeautifulSoup(target, "xml")

for body in soup.select("body"):
    for forecast in body.select("onemonth_ta_forecast"):
        for ta in forecast.select("local_ta"):
            print("도시:", ta.select_one("local_ta_name").string)
            print("평년기온:", ta.select_one("week1_local_ta_normalYear").string)
            print("1주차 평년비슷범위:", ta.select_one("week1_local_ta_similarRange").string)
            print("1주차 지역 기온 예보 확률(낮음):", ta.select_one("week1_local_ta_minVal").string)
            print("1주차 지역 기온 예보 확률(비슷):", ta.select_one("week1_local_ta_similarVal").string)
            print("1주차 지역 기온 예보 확률(높음):", ta.select_one("week1_local_ta_maxVal").string)
            print()