#!/usr/bin/python3
''' Using Reddit api to get the total number of suscribers of a subreddit '''
from requests import get


def number_of_subscribers(subreddit):
    ''' Return the number of suscribers of a subreddit '''
    html = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
               allow_redirects=False)
    if html.status_code == 200:
        return html.json()['data']['suscribers']
    return 0
