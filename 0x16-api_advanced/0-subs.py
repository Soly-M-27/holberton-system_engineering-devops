#!/usr/bin/python3
''' function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given
subreddit '''

import request


def number_of_subscribers(subreddit):
    ''' Returns total number of subs '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'User Agent'}
    response = request.get(url, header=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    else:
        return response.json().get('data').get('subscribers')
