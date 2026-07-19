#!/usr/bin/env python3
"""
Social Media scanner — cari jejak nomor di sosial media Indonesia
"""

import json
from lib.output import *
from lib.request import send
from lib.googlesearch import search

def scan(numberObj):
    number = numberObj.get('default', '')
    localNumber = numberObj.get('local', '')
    internationalNumber = numberObj.get('international', '')
    numberCountryCode = numberObj.get('countryCode', '+62')

    info("=== JEJAK SOSIAL MEDIA ===")

    # Google dork untuk social media Indonesia
    sites = [
        ("Facebook", "site:facebook.com \"{}\"", 5),
        ("Instagram", "site:instagram.com \"{}\"", 5),
        ("Twitter/X", "site:twitter.com \"{}\"", 3),
        ("TikTok", "site:tiktok.com \"{}\"", 3),
        ("LinkedIn", "site:linkedin.com \"{}\"", 3),
        ("Tokopedia", "site:tokopedia.com \"{}\"", 3),
        ("Shopee", "site:shopee.co.id \"{}\"", 3),
        ("Kaskus", "site:kaskus.co.id \"{}\"", 3),
    ]

    found_data = []
    for name, dork, stop in sites:
        query = dork.format(number, localNumber, internationalNumber)
        try:
            results = search(query, stop=stop)
            if results:
                for url in results:
                    print(f"  ✅ {name}: {url}")
                    found_data.append({'site': name, 'url': url})
            else:
                print(f"  ⬜ {name}: Tidak ditemukan")
        except:
            print(f"  ⬜ {name}: Gagal scan")

    # Google Maps lookup jika ada data ditemukan
    if found_data:
        info("=== LOKASI (GOOGLE MAPS) ===")
        for data in found_data[:3]:
            try:
                # Cari alamat dari hasil sosial media
                import requests
                r = requests.get(data['url'], timeout=8, 
                    headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S908E) AppleWebKit/537.36'})
                if r.status_code == 200:
                    # Extract location info dari halaman
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(r.text, 'html.parser')
                    
                    # Cari teks yang mengandung alamat
                    text = soup.get_text()
                    import re
                    # Cari pattern alamat Indonesia
                    address_patterns = [
                        r'(Jl\.\s*[^,]+,\s*[^,]+,\s*[A-Za-z\s]+)',
                        r'(Kota\s+[A-Za-z]+)',
                        r'(Jakarta|Bandung|Surabaya|Medan|Makassar|Yogyakarta|Denpasar|Palembang|Semarang|Malang|Bogor|Pekanbaru|Banjarmasin|Balikpapan|Padang|Lampung)',
                    ]
                    for pattern in address_patterns:
                        match = re.search(pattern, text)
                        if match:
                            addr = match.group(0).strip()[:100]
                            maps_url = f"https://www.google.com/maps/search/{requests.utils.quote(addr)}"
                            print(f"  📍 Dari {data['site']}: {addr}")
                            print(f"  🗺️  Maps: {maps_url}")
                            break
            except:
                pass
    else:
        info("=== LOKASI ===")
        warning("Tidak ada data sosial media untuk dilacak lokasinya")

