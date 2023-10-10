#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    if len(hot_list) >= 100:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'My Reddit API Client'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
