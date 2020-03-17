import requests
import re
import time
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv("./univ/base.csv")


def kangwon():
    # 강원대학교 추천도서는 20200316 기준으로 155페이지
    df_index = 0
    for page in range(1, 156):
        res = requests.get(f'http://lib.kangwon.ac.kr:8080/board/list_book.jsp?pg={page}&bcs=60&re=1')
        soup = BeautifulSoup(res.content, 'html.parser')
        sel = soup.select('td > div')
        for title in sel:
            line = title.get_text()
            re.sub("[\r\t\n\xa0]", "", line).split("   ")
            df.loc[df_index] = [line.split("   ")[0].strip(), line.split("   ")[2].split(":")[1].strip(),
                                line.split("   ")[3].split(":")[1].strip()]
            df_index += 1
        time.sleep(0.5)
    df.to_csv("../output/kangwon.csv", encoding="utf-8-sig", index=False)
    print("crawlbooks/output/kangwon.csv is saved")


def gyeongsang():
    # 경상대학교 교양권장 100선은 10권씩 10페이지
    df_index = 0
    for page in range(1, 11):
        res = requests.get(f'http://books.gnu.ac.kr/local/recommend/recommend100List.do?pageNo={page}')
        soup = BeautifulSoup(res.content, 'html.parser')
        titles = soup.find_all('li', {'class': 'tcol_2'})
        authors = soup.find_all('li', {'class': 'tcol_3'})
        publishers = soup.find_all('li', {'class': 'tcol_4'})

        for i in range(1, 11):
            title = titles[i].get_text().strip()
            author = authors[i].get_text().strip()
            publisher = publishers[i].get_text().strip()
            if title == author == publisher == "":
                continue
            df.loc[df_index] = [title, author, publisher]
            df_index += 1
        time.sleep(0.5)
    df.to_csv("../output/gyeongsang.csv", encoding="utf-8-sig", index=False)
    print("crawlbooks/output/gyeongsang.csv is saved")
