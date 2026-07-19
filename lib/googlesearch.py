#!/usr/bin/env python3
"""Google search helper - simplified"""

import requests
from bs4 import BeautifulSoup

def search(query, stop=5):
    """Simple Google search — return list of URLs"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S908E) AppleWebKit/537.36',
    }
    params = {'q': query, 'num': stop}
    try:
        r = requests.get('https://www.google.com/search', params=params, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        urls = []
        for a in soup.select('a[href^="/url?q="]'):
            url = a['href'].replace('/url?q=', '').split('&')[0]
            if url not in urls:
                urls.append(url)
        return urls[:stop]
    except:
        return []

def closeBrowser():
    pass
