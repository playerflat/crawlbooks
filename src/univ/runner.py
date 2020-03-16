import requests
import re
import time
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv("./univ/base.csv")


def kangwon():
    # 강원대학교 추천도서는 20200316 기준으로 155페이지
    df_index = 0
    for pages in range(1, 156):
        res = requests.get(f'http://lib.kangwon.ac.kr:8080/board/list_book.jsp?pg={pages}&bcs=60&re=1')
        soup = BeautifulSoup(res.content, 'html.parser')
        sel = soup.select('td > div')
        for title in sel:
            line = title.get_text()
            re.sub("[\r\t\n\xa0]", "", line).split("   ")
            df.loc[df_index] = [line.split("   ")[0].strip(), line.split("   ")[2].split(":")[1].strip(),
                                line.split("   ")[3].split(":")[1].strip()]
            df_index += 1
        # print(soup.select('td > div > a > b'))
        time.sleep(0.5)
    df.to_csv("../output/kangwon.csv", encoding="utf-8-sig", index=False)
