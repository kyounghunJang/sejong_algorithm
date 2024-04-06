import os
from notion_client import Client
import requests
from datetime import datetime
import pytz
import argparse

korea_tz = pytz.timezone('Asia/Seoul')
now = datetime.now(korea_tz)
now_str = now.strftime("%Y-%m-%d %H:%M:%S")

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
response = requests.get(f"https://api.github.com/repos/kyounghunJang/2024_Capstone/commits", headers=headers)
response.raise_for_status()

# 최근 커밋의 작성자 정보
latest_commit = response.json()[0]
author = latest_commit["commit"]["author"]["name"]

notion = Client(auth=args.notion_token)

dec="완료"

my_page = notion.pages.create(
    parent={"database_id": "64e18e30b01e4b43890b2c15fec1d840"},
    properties={
        "Date": {"title": [{"type": "text", "text": {"content": now_str}}]},
        "Name": {"rich_text": [{"type": "text", "text": {"content": author }}]},
        "Description": {"rich_text": [{"type": "text", "text": {"content":dec}}]},
    },
)


