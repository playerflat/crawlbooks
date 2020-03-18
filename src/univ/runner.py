import requests
import re
import time
import pandas as pd
from bs4 import BeautifulSoup


def kangwon():
    # 강원대학교 추천도서는 5권씩 155페이지 (20200316)
    df = pd.read_csv("./univ/base.csv")
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
        print(f'kangwon {df_index}')
    df.to_csv("../output/kangwon.csv", encoding="utf-8-sig", index=False)
    print("crawlbooks/output/kangwon.csv is saved")


def gyeongsang():
    # 경상대학교 교양권장 100선은 10권씩 10페이지 (20200317)
    df = pd.read_csv("./univ/base.csv")
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
        print(f'gyeongsang {df_index}')
    df.to_csv("../output/gyeongsang.csv", encoding="utf-8-sig", index=False)
    print("crawlbooks/output/gyeongsang.csv is saved")


def mokwon():
    # 목원대학교 리딩목원 2018 추천도서는 120권 (20200318)
    df = pd.read_csv("./univ/base.csv")
    df_index = 0
    for page in range(1196, 1316):  # 1316
        res = requests.get(
            f'https://liberalarts.mokwon.ac.kr/sub0401/articles/view/tableid/recommended/category/7/id/{page}')
        soup = BeautifulSoup(res.content, 'html.parser')
        title = soup.select_one(' tr > td > strong')
        author = soup.find('font', {'color': '#ff0000'})
        title = title.text[3:]
        try:
            if title[0] == " ":
                title = title[1:]
        except IndexError:
                title = " "
        if author is not None:
            author = re.sub('[0-9.~]', '', author.text.split("/")[0]).strip()
        else:
            author = ""
        df.loc[df_index] = [title, author, ""]
        df_index += 1
        time.sleep(0.5)
        print(f'mokwon {df_index}')
    df.to_csv("../output/mokwon.csv", encoding="utf-8-sig", index=False)
    print("crawlbooks/output/mokwon.csv is saved")
