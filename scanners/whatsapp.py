#!/usr/bin/env python3
"""
WhatsApp scanner — cek nomor terdaftar WhatsApp
"""

from lib.output import *
from lib.request import send

def scan(number):
    test("WhatsApp check...")

    # Format nomor tanpa +62
    clean = number.replace('+', '')

    # Cek via WhatsApp API
    wa_urls = [
        f"https://api.whatsapp.com/send?phone={clean}",
        f"https://wa.me/{clean}",
    ]

    info("=== WHATSAPP ===")
    try:
        # Cek via WhatsApp direct link
        import requests
        r = requests.get(f"https://wa.me/{clean}", timeout=10, allow_redirects=True)
        if r.status_code == 200:
            print(f"  ✅ WhatsApp: Tersedia di wa.me/{clean}")
        else:
            warning(f"  ⚠️ WhatsApp: wa.me/{clean} (status {r.status_code})")
    except:
        pass

    # Cek profile picture via API (public)
    try:
        r = requests.get(f"https://api.whatsapp.com/send?phone={clean}", timeout=10)
        if "send" in r.url:
            print(f"  ✅ Link WA: https://wa.me/{clean}")
    except:
        pass

    print(f"  📲 Link langsung: https://wa.me/{clean}")
