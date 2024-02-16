#!/usr/bin/python3
"""function that returns the number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Gets number of subscribers
       Args:
           subreddit (str): name of subreddit
       Returns:
           number of subscribers if valid, 0 otherwise
    """
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    
    try:
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            
            return subscribers
        else:
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return 0
