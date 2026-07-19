#!/usr/bin/env python3
"""Format helpers"""

import re

def formatNumber(number):
    """Format nomor HP ke format internasional"""
    clean = re.sub(r'[^0-9]', '', str(number))
    if clean.startswith('0'):
        clean = '62' + clean[1:]
    elif clean.startswith('62'):
        pass
    else:
        clean = '62' + clean
    return clean

def formatNumberLocal(number):
    """Format ke format lokal (08xx)"""
    clean = re.sub(r'[^0-9]', '', str(number))
    if clean.startswith('62'):
        clean = '0' + clean[2:]
    elif not clean.startswith('0'):
        clean = '0' + clean
    return clean
