#!/usr/bin/python3
""" implment recurse func """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    A recursive function that queries the Reddit API,
    and returns a list containing the titles of all hot articles
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'custom user-agent'}

    response = requests.get(url,
                            params=params,
                            headers=headers,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get('data', {})
    for post in data.get('children', []):
        hot_list.append(post.get('data').get('title'))

    if data.get('after'):
        return recurse(subreddit, hot_list, data.get('after'))
    else:
        return hot_list
