#!/usr/bin/env python3
"""
Numverify scanner — info nomor dari numverify.com
"""

import hashlib
from bs4 import BeautifulSoup
from lib.output import *
from lib.request import send

def scan(number):
    test("Numverify scan...")
    try:
        requestSecret = ''
        res = send('GET', 'https://numverify.com/')
        soup = BeautifulSoup(res.text, "html5lib")
    except:
        error("Numverify.com tidak bisa diakses")
        return

    for tag in soup.find_all("input", type="hidden"):
        if tag['name'] == "scl_request_secret":
            requestSecret = tag['value']
            break

    apiKey = hashlib.md5((number + requestSecret).encode('utf-8')).hexdigest()
    res = send('GET', 'https://numverify.com/php/handler.php',
               params={'secret': apiKey, 'number': number, 'scl_request_secret': requestSecret})

    try:
        data = res.json()
        if data.get('valid'):
            info("=== NUMVERIFY ===")
            print(f"  📱 Nomor valid  : ✅ Ya")
            print(f"  🌍 Negara       : {data.get('country_name', 'N/A')}")
            print(f"  🏢 Provider     : {data.get('carrier', 'N/A')}")
            print(f"  📋 Tipe         : {data.get('line_type', 'N/A')}")
        else:
            warning("Numverify: Nomor tidak valid atau tidak ditemukan")
    except:
        warning("Numverify: Gagal parse response")
