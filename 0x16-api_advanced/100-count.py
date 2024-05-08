#!/usr/bin/python3
""" Count words using recursive function """

import requests
import sys
from collections import defaultdict


def count_words(subreddit, word_list):
    """
    A recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of keywords to count occurrences for.

    Returns:
        None
    """
    counts = defaultdict(int)
    _count_words_recursive(subreddit, set(word_list), counts)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
    for keyword, count in sorted_counts:
        print(f"{keyword.lower()}: {count}")


def _count_words_recursive(subreddit, word_set, counts, after=None):
    """
    A recursive helper function to query the Reddit API,
    and count occurrences of keywords.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_set (set): A set of keywords to count occurrences for.
        counts (dict): A dictionary to store keyword counts.
        after (str): A token used for pagination in Reddit API responses.

    Returns:
        None
    """
    if not word_set:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'MyApp'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        for post in data['data']['children']:
            title = post['data']['title']
            if title:
                for keyword in word_set:
                    if keyword in title.lower().split():
                        counts[keyword] += 1

        after = data['data']['after']
        if after:
            _count_words_recursive(subreddit, word_set, counts, after)
    except requests.RequestException as e:
        print("Error:", e)
