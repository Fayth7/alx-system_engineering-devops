#!/usr/bin/python3
"""
Queries Reddit API, prints top ten hot posts of a subreddit
"""
import re
import requests
import sys


def count_words(subreddit, word_list, after=None, word_count={}):
    if after is None:
        sorted_results = sorted(
            word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_results:
            print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'My Reddit API Client'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()  # Convert to lowercase
            for word in word_list:
                if word.lower() in title:
                    if word.lower() in word_count:
                        word_count[word.lower()] += 1
                    else:
                        word_count[word.lower()] = 1

        after = data['data']['after']

        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            count_words(subreddit, word_list, None, word_count)
    else:
        return


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
