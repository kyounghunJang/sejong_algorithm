import os
from notion_client import Client
import requests
from datetime import datetime
import pytz
import argparse

korea_tz = pytz.timezone('Asia/Seoul')
now = datetime.now(korea_tz)
now_str = now.strftime("%Y-%m-%d")

parser = argparse.ArgumentParser(description='Process some tokens.')
parser.add_argument('--github_token', type=str, help='GitHub API token')
parser.add_argument('--notion_token', type=str, help='Notion client authentication token')

args = parser.parse_args()


# GitHub API 토큰
token = args.github_token

# API 요청 헤더
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

# 최근 커밋 정보를 얻는 API 요청
response = requests.get(f"https://api.github.com/repos/kyounghunJang/sejong_algorithm/commits", headers=headers)
response.raise_for_status()
latest_commit = response.json()[0]
author = latest_commit["commit"]["author"]["name"]

notion = Client(auth=args.notion_token)

dec="완료"

# 오늘 날짜에 해당하는 페이지가 이미 있는지 확인
database_id = "64e18e30b01e4b43890b2c15fec1d840"
pages = notion.databases.query(database_id=database_id)

cnt=0
for page in pages["results"]:
    if cnt >2:
        break
    page_date = page["properties"]["Date"]["title"][0]["text"]["content"]
    page_author = page["properties"]["Name"]["rich_text"][0]["text"]["content"]
    if page_date == now_str and page_author == author:
        print(f"{author}는 이미 오늘 날짜에 페이지를 작성했습니다.")
        break
    cnt+=1
    
else:
    # 오늘 날짜에 해당하는 페이지가 없으면 새 페이지를 만듭니다.
    my_page = notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Date": {"title": [{"type": "text", "text": {"content": now_str}}]},
            "Name": {"rich_text": [{"type": "text", "text": {"content": author }}]},
            "Description": {"rich_text": [{"type": "text", "text": {"content":dec}}]},
        },
    )