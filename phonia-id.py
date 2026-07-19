#!/usr/bin/env python3
"""
PHONIA-ID — Indonesian Phone Number OSINT Toolkit
Original: Phonia Toolkit by Entynetproject
Rebrand + Indonesia support by DevCult XII

Scan nomor HP Indonesia: cek provider, lokasi, social media, WhatsApp, dll
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

from lib.args import args, parser
from lib.banner import banner, __version__
from lib.output import *
from lib.format import *

from scanners import localscan
from scanners import numverify
from scanners import sosial_media
from scanners import whatsapp
from scanners import provider_id

def scan_number(InputNumber):
    os.system("clear")
    print(banner)
    time.sleep(1)
    title(f"[!] Scan nomor: {InputNumber} [!]")
    time.sleep(1)

    number = localscan.scan(InputNumber)
    if not number:
        error("Gagal parse nomor. Cek format nomor.")
        return

    numverify.scan(number['default'])
    provider_id.scan(number['local'], number['countryIsoCode'])
    sosial_media.scan(number)
    whatsapp.scan(number['default'])

if __name__ == "__main__":
    parser.description = "Phonia-ID — OSINT untuk nomor Indonesia"
    args = parser.parse_args()

    if args.number:
        scan_number(args.number)
    elif args.input:
        with open(args.input) as f:
            for line in f:
                n = line.strip()
                if n:
                    print("\n" + "="*60)
                    scan_number(n)
                    print("="*60)
    else:
        parser.print_help()
