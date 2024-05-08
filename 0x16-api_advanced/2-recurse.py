#!/usr/bin/python3

'Gets top 10 most host posts of a subreddit using reddit api.'
import requests
import time


def recurse(subreddit, hot_list=[], params=None):
    """Gets top 10 most host posts of a subreddit using reddit api."""

    headers = {'User-Agent': 'alxAPI'}

    res = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers=headers,
        allow_redirects=False,
        params=params
    )

    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        hot_list.extend(posts)
        after = res.json().get('data').get('after')
        if after:
            params = {'after': after}
            return recurse(subreddit, hot_list, params)
        else:
            return hot_list
    elif res.status_code == 429:
        time.sleep(1)
        return recurse(subreddit, hot_list, params)
    else:
        return None
