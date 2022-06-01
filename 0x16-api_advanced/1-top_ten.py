#!/usr/bin/python3
''' queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit '''

import json
import requests


def top_ten(subreddit):
    ''' prints top 10 hot posts for a given subreddit '''
    url = "https://www.reddit.com/r/"
    headers = {'User-Agent': 'Its a me'}
    response = requests.get(url + subreddit + "/hot.json?limit=10",
                            headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
    else:
        for x in response.json().get('data').get('children'):
            print(x.get('data').get('title'))
