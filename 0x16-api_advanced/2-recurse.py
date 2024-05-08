#!/usr/bin/python3
""" Using recrsion to get title of top 10 hot posts"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return list of titles for all hot posts on 
    subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    headers = {"User-Agent": "MyApp"}
    response = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
