#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    # Construct the URL for the subreddit's about page in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if the 'subscribers' key is present in the response
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            # 'subscribers' key not found (invalid subreddit)
            return 0
    else:
        # Invalid subreddit or other error
        return 0
