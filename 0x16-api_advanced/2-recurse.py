#!/usr/bin/python3
""" implment recurse func """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    A recursive function that queries the Reddit API,
    and returns a list containing the titles of all hot articles
    """
    if hot_list is None:
        hot_list = []  # Initialize hot_list if not provided

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'MyApp'}
    response = requests.get(url, headers=headers)

    # Check for successful response
    if response.status_code != 200:
        print("Error:", response.status_code)
        return None

    data = response.json().get('data', {})

    # Check if 'children' key exists in the data
    if 'children' in data:
        # Extract titles of hot posts
        for post in data['children']:
            hot_list.append(post['data'].get('title'))

        # Recursively call the function if there are more pages
        if data.get('after'):
            return recurse(subreddit, hot_list, data['after'])
        else:
            return hot_list
    else:
        print("Error: Unexpected response format")
        return None
