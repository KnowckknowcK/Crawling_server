## Spider 아키텍쳐
![image](https://github.com/KnowckknowcK/Crawling_server/assets/104684033/e35190ff-94b8-4c5a-bbe8-02b57f0441a9)

<br>

## 기술스택
언어 및 프레임워크: `Python3.10`, `Scrapy`

주요 라이브러리: `BeautifulSoup`, `trafilatura`, `logging`

인프라: `AWS/EC2`, `Linux Crontab` 

<br>

## 실행방법

### 환경변수
최상위 경로에 .env 파일 위치
```yaml
DB_HOST = {호스트명}
DB_USER = {사용자명}
DB_PASSWORD = {비밀번호}
DB_SCHEMA = {데이터베이스 이름}
```

### 로컬 실행방법
```powershell
# 필요한 모듈 설치
pip install -r requirements.txt

# 디렉토리 이동
cd knowckknowck_crawling

# 실행
python -m naver_crawler
python -m rss_crawler
```

### vm 실행방법
```powershell
# 디렉토리 이동
cd ~/Crawling_server/knowckknowck_crawling

# 실행
python3 -m naver_crawler &
python3 -m rss_crawler &
```
```powershell
# 홈 경로에 실행 스크립트 위치
./execute_crawler_1.sh
./execute_crawler_2.sh
```

## Crontab 설정
```bash
.---------------- minute (0 - 59)
|  .------------- hour (0 - 23)
|  |  .---------- day of month (1 - 31)
|  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
|  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
|  |  |  |  |
*  *  *  *  * user-name command to be executed
0  2  *  *  * /home/ubuntu/execute_crawler_1.sh
0  3  *  *  * /home/ubuntu/execute_crawler_2.sh
```
