#!/usr/bin/python3
""" count words usong recursive function """
import requests


def count_words(subreddit, word_list):
    """
    A recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted count of given keywords.
    """
    # Initialize counts dictionary
    counts = {}

    # Call the recursive helper function
    _count_words_recursive(subreddit, word_list, counts)

    # Sort counts by count (descending) and keyword (ascending)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
    for keyword, count in sorted_counts:
        print(f"{keyword.lower()}: {count}")

def _count_words_recursive(subreddit, word_list, counts, after=None):
    """
    A recursive helper function to query the Reddit API and count occurrences of keywords.
    """
    # Base case: if word_list is empty, return
    if not word_list:
        return

    # Get the first keyword from the word_list
    keyword = word_list[0].lower()

    # Reddit API endpoint for hot posts in the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyApp'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Extract titles of hot posts
        for post in data['data']['children']:
            title = post['data']['title']
            # Count occurrences of the keyword in the title
            if keyword in title.lower().split():
                counts[keyword] = counts.get(keyword, 0) + 1

        # Check if there are more pages of results
        after = data['data']['after']
        # Recursively call _count_words_recursive with the next keyword and updated counts
        _count_words_recursive(subreddit, word_list[1:], counts, after)
    elif response.status_code == 404:
        # If subreddit is not found, return
        return
    else:
        # Handle other error cases
        print("Error:", response.status_code)
        return
