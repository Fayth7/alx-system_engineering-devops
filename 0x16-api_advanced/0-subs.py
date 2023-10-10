#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'My Reddit API Client'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response to extract the subscriber count
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is invalid or any other error occurs, return 0
        return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
