#!/usr/bin/python3
""" implment recurse func """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    A recursive function that queries the Reddit API,
    and returns a list containing the titles of all hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'MyApp'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return None
    data = response.json().get('data', {})
    for post in data.get('children', []):
        hot_list.append(post.get('data').get('title'))

    if data.get('after'):
        return recurse(subreddit, hot_list, data.get('after'))
    else:
        return hot_list
