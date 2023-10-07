import os
import requests
import json
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

# 从环境变量中获取Bearer Token
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# 设置请求头，以便在所有API请求中使用
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "User-Agent": "v2RecentSearchPython"
}

def get_following_tweets():
    url = "https://api.twitter.com/2/users/micarfield/following"
    response = requests.get(url, headers=headers)
    
    # 其他代码...
    if response.status_code != 200:
        print(f"Failed to retrieve following: {response.status_code}")
        print(response.text)
        return []  # 返回一个空列表而不是None

if __name__ == "__main__":
    tweets = get_following_tweets()
    if tweets:  # 检查tweets是否非空
        for tweet in tweets:
            print(f"{tweet['author_id']}: {tweet['text']}")