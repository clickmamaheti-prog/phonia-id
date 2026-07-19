#!/usr/bin/env python3
"""HTTP request helper"""

import requests

SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S908E) AppleWebKit/537.36',
    'Accept': 'text/html,application/json,*/*',
})

def send(method, url, **kwargs):
    """Send HTTP request"""
    kwargs.setdefault('timeout', 15)
    kwargs.setdefault('verify', False)
    return SESSION.request(method, url, **kwargs)
