#!/usr/bin/python3

'Gets top 10 most host posts of a subreddit using reddit api.'
import requests
import time


def recurse(subreddit, hot_list=[], params=None):
    """Gets top 10 most host posts of a subreddit using reddit api."""
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
