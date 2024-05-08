#!/usr/bin/python3

'Prints a sorted count of given keywords in each hot title from subreddit.'
import requests
import time


def count_word(post, word_list, word_count):
    if len(word_list) > 0:
        title = post.get('data').get('title')
        word_l = word_list[0].lower()
        count = title.lower().count(word_l)
        if count:
            word_count[word_l] = count + word_count.get(word_l, 0)
        count_word(post, word_list[1::], word_count)


def count_all(posts, word_list, word_count):
    if len(posts) > 0:
        count_word(posts[0], word_list, word_count)
        count_all(posts[1::], word_list, word_count)


def count_words(subreddit, word_list, params=None, word_count={}):
    headers = {'User-Agent': 'alxAPI'}

    res = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers=headers,
        allow_redirects=False,
        params=params
    )

    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        count_all(posts, word_list, word_count)
        after = res.json().get('data').get('after')
        if after:
            params = {'after': after}
            count_words(subreddit, word_list, params, word_count)
        else:
            sorted_count = dict(
                sorted(word_count.items(), key=lambda i: i[1], reverse=True)
            )
            for k, v in sorted_count.items():
                print('{}: {}'.format(k, v))
    elif res.status_code == 429:
        time.sleep(1)
        count_words(subreddit, word_list, params, word_count)
