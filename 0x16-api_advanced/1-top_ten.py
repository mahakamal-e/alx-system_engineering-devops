#!/usr/bin/python3
""" implment top_ten func """
import requests


def top_ten(subreddit):
    """"Queries the Reddit API and prints the first 10 hot posts titles"""
     url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
     headers = {'User-Agent': 'MyApp'}
     response = requests.get(url, headers=headers)
      if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    elif response.status_code == 404:
        print(None)
    else:
        print("Error:", response.status_code)
