#!/usr/bin/python3
""" implement recurse func """
import requests


def recurse(subreddit, hot_list=[], params=None):
    """
    queries the Reddit API and returns a list,
    containing the titles of all hot articles
    for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyApp'}

    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)

    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        hot_list.extend(posts)
        after = response.json().get('data').get('after')
        if after:
            params = {'after': after}
            return recurse(subreddit, hot_list, params)
        else:
            return hot_list
    else:
        return None
