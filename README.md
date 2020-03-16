# crawlbooks

대학 도서관의 추천도서 목록을 수집하기 위해 제작되었습니다.

#### 사용처
- 추천도서 목록을 pdf, xls(x), hwp 등으로 제공하지 않는 대학 도서관

#### 지원되는 곳
- [강원대학교 도서관](http://lib.kangwon.ac.kr:8080/board/list_book.jsp?pg=1&bcs=60&re=1)
- 발견하고 필요하면 추가 예정

#### 실행 안될 때
- 사이트 url이나 html이 수정되었을 때
- 의심스러운 접근으로 IP차단 당했을 때

#### 주의점
- 서버에 부하를 줄 수 있으니 비슷한 시간에 여러번 사용하지 말 것

#### 개발에 사용한 것
- Python 3.8 (Pycharm 2019.3.3)
- beautifulsoup4 4.8.2
- pandas 1.0.2
- requests 2.23.0

#### 기타
- pandas 설치 중 C++ Build Tools 오류 뜰 때는 [여기서](https://visualstudio.microsoft.com/ko/vs/older-downloads/) [재배포 가능 패키지 및 빌드 도구] - Microsoft Build Tools 2015 업데이트 3 설치 후 재부팅
