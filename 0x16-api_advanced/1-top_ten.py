#!/usr/bin/python3
"""top 10 hot posts on a subreddit"""

import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    data = response.json()

    if response.status_code == 200:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
