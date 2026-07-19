#!/usr/bin/env python3
"""
Indonesia Provider Database — identifikasi provider berdasarkan prefix
"""

from lib.output import *

# Database prefix nomor Indonesia
PROVIDER_DATA = {
    'Telkomsel': {
        'prefix': ['0811','0812','0813','0821','0822','0823','0851','0852','0853'],
        'jenis': ['KartuHalo (Pascabayar)', 'SimPATI (Prabayar)', 'By.U (Prabayar)'],
        'website': 'https://www.telkomsel.com',
    },
    'Indosat': {
        'prefix': ['0814','0815','0816','0855','0856','0857','0858'],
        'jenis': ['IM3 (Prabayar)', 'Mentari (Prabayar)', 'Matrix (Pascabayar)'],
        'website': 'https://www.indosatooredoo.com',
    },
    'XL Axiata': {
        'prefix': ['0817','0818','0819','0859','0877','0878','0879'],
        'jenis': ['XL Prabayar', 'XL Pascabayar', 'XL Prioritas'],
        'website': 'https://www.xl.co.id',
    },
    'Tri/3': {
        'prefix': ['0895','0896','0897','0898','0899'],
        'jenis': ['Tri Prabayar', 'Tri Pascabayar'],
        'website': 'https://www.tri.co.id',
    },
    'Smartfren': {
        'prefix': ['0881','0882','0883','0884','0885','0886','0887','0888','0889'],
        'jenis': ['Smartfren Prabayar', 'Smartfren Pascabayar'],
        'website': 'https://www.smartfren.com',
    },
    'Axis': {
        'prefix': ['0831','0832','0833','0838'],
        'jenis': ['Axis Prabayar'],
        'website': 'https://www.axis.co.id',
    },
    'Bolt': {
        'prefix': ['0921','0922'],
        'jenis': ['Bolt 4G'],
        'website': 'https://www.bolt.id',
    },
    'By.U': {
        'prefix': ['0851','0852','0853'],
        'jenis': ['By.U Prabayar (Telkomsel)'],
        'website': 'https://www.byu.id',
    },
}

def detect_provider(number):
    """Deteksi provider dari nomor"""
    clean = number.replace('+62', '0').replace('-', '').replace(' ', '')
    if not clean.startswith('0'):
        clean = '0' + clean

    for provider, data in PROVIDER_DATA.items():
        for prefix in data['prefix']:
            if clean.startswith(prefix):
                return provider, data
    return None, None

def scan(number, countryIsoCode):
    if countryIsoCode != 'ID':
        warning(f"Bukan nomor Indonesia ({countryIsoCode})")
        return

    info("=== PROVIDER INDONESIA ===")
    provider, data = detect_provider(number)
    if provider and data:
        print(f"  🏢 Provider       : {provider}")
        print(f"  📋 Jenis          : {', '.join(data['jenis'])}")
        print(f"  🌐 Website        : {data['website']}")
    else:
        warning("Provider tidak dikenal (mungkin nomor baru)")
