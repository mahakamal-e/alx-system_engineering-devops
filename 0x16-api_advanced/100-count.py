#!/usr/bin/python3
"""Implement count_words function"""

import requests
import time


def fetch_hot_articles(subreddit, limit=100, after=None, titles=[]):
    """
    Args:

    Returns:
    list: A list containing the titles of the fetched articles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'YOUR_USER_AGENT'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            titles.append(post['data']['title'].lower())
        after = data['data']['after']
        if after:
            time.sleep(2)
            return fetch_hot_articles(subreddit, limit, after, titles)
        else:
            return titles
    else:
        return None


def count_words(subreddit, word_list, titles=[], counts={}):
    """
    Returns:
    None
    """
    titles = fetch_hot_articles(subreddit)

    if not titles:
        return

    for title in titles:
        for word in word_list:
            if word.lower() in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + 1
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
