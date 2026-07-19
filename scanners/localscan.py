#!/usr/bin/env python3
"""
Local scan — parse nomor HP Indonesia
"""

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from lib.format import *
from lib.output import *

PROVIDER_ID = {
    'Telkomsel': ['0811', '0812', '0813', '0821', '0822', '0823', '0851', '0852', '0853'],
    'Indosat': ['0814', '0815', '0816', '0855', '0856', '0857', '0858'],
    'XL': ['0817', '0818', '0819', '0859', '0877', '0878', '0879'],
    'Tri/3': ['0895', '0896', '0897', '0898', '0899'],
    'Smartfren': ['0881', '0882', '0883', '0884', '0885', '0886', '0887', '0888', '0889'],
    'Axis': ['0831', '0832', '0833', '0838'],
    'By.U': ['0851', '0852', '0853'],
    'Bolt': ['0921', '0922'],
}

def detect_provider_id(number):
    """Deteksi provider berdasarkan prefix nomor"""
    clean = number.replace('+62', '').replace('0', '', 1) if number.startswith('0') else number.replace('+62', '')
    for provider, prefixes in PROVIDER_ID.items():
        for prefix in prefixes:
            if clean.startswith(prefix.replace('0', '')):
                return provider
    return 'Unknown'

def scan(InputNumber, print_results=True):
    test('Local scan...')

    FormattedPhoneNumber = "+" + formatNumber(InputNumber)

    try:
        PhoneNumberObject = phonenumbers.parse(FormattedPhoneNumber, None)
    except Exception as e:
        throw(str(e))
        return False

    if not phonenumbers.is_valid_number(PhoneNumberObject):
        error("Nomor HP tidak valid!")
        return False

    number = phonenumbers.format_number(
        PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace('+', '')
    numberCountryCode = phonenumbers.format_number(
        PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
    numberCountry = phonenumbers.region_code_for_country_code(
        int(numberCountryCode))

    localNumber = phonenumbers.format_number(
        PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace(numberCountryCode, '')
    internationalNumber = phonenumbers.format_number(
        PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    country = geocoder.country_name_for_number(PhoneNumberObject, "en")
    location = geocoder.description_for_number(PhoneNumberObject, "id")
    
    # Fallback lokasi via prefix/kode area Indonesia
    if not location or location == "Indonesia":
        area_codes = {
            '021': 'Jakarta, Bogor, Depok, Tangerang, Bekasi',
            '022': 'Bandung, Cimahi',
            '024': 'Semarang',
            '0274': 'Yogyakarta, Sleman, Bantul',
            '031': 'Surabaya, Gresik, Bangkalan',
            '0341': 'Malang, Batu',
            '0361': 'Denpasar, Bali',
            '0411': 'Makassar, Maros',
            '0511': 'Samarinda',
            '0522': 'Banjarmasin',
            '0542': 'Balikpapan',
            '061': 'Medan, Binjai',
            '0711': 'Palembang',
            '0737': 'Lampung',
            '0751': 'Padang',
            '0761': 'Pekanbaru',
        }
        clean_local = localNumber
        for code, area in sorted(area_codes.items(), key=lambda x: -len(x[0])):
            if clean_local.startswith(code):
                location = area
                break
    
    # Cek provider + kemungkinan lokasi dari prefix mobile Indonesia
    if not location or location == "Indonesia":
        clean_prefix = localNumber
        if not clean_prefix.startswith('0'):
            clean_prefix = '0' + clean_prefix
        mobile_areas = {
            '0811': 'Telkomsel (Jabodetabek)',
            '0812': 'Telkomsel (Nasional)',
            '0813': 'Telkomsel (Nasional)',
            '0821': 'Telkomsel (Sumatera)',
            '0822': 'Telkomsel (Kalimantan)',
            '0823': 'Telkomsel (Sulawesi)',
            '0851': 'Telkomsel/By.U (Nasional)',
            '0852': 'Telkomsel/By.U (Nasional)',
            '0853': 'Telkomsel/By.U (Nasional)',
            '0814': 'Indosat (Jawa)',
            '0815': 'Indosat (Jawa Timur)',
            '0816': 'Indosat (Nasional)',
            '0855': 'Indosat (Sumatera)',
            '0856': 'Indosat (Nasional)',
            '0857': 'Indosat (Nasional)',
            '0858': 'Indosat (Kalimantan)',
            '0817': 'XL (Jabodetabek)',
            '0818': 'XL (Nasional)',
            '0819': 'XL (Nasional)',
            '0859': 'XL (Nasional)',
            '0877': 'XL (Nasional)',
            '0878': 'XL (Nasional)',
            '0831': 'Axis (Nasional)',
            '0832': 'Axis (Nasional)',
            '0881': 'Smartfren (Nasional)',
            '0882': 'Smartfren (Nasional)',
            '0895': 'Tri/3 (Nasional)',
            '0896': 'Tri/3 (Nasional)',
        }
        for prefix, area in sorted(mobile_areas.items(), key=lambda x: -len(x[0])):
            if clean_prefix.startswith(prefix):
                location = area
                break
    
    carrierName = carrier.name_for_number(PhoneNumberObject, 'id')
    providerId = detect_provider_id(FormattedPhoneNumber)

    if print_results:
        info("=== INFORMASI DASAR ===")
        print(f"  📱 Nomor       : {internationalNumber}")
        print(f"  🌍 Negara      : {country} ({numberCountry})")
        print(f"  📍 Wilayah     : {location or 'N/A'}")
        print(f"  🏢 Provider    : {carrierName or providerId}")
        print(f"  📋 Tipe        : {'Prabayar' if len(localNumber) > 9 else 'Pascabayar/Kantor'}")

    # Timezone
    try:
        tz_list = timezone.time_zones_for_number(PhoneNumberObject)
        if tz_list:
            if print_results:
                print(f"  🕐 Timezone    : {', '.join(tz_list)}")
    except:
        pass

    numberObj = {
        'default': number,
        'local': localNumber,
        'international': internationalNumber,
        'countryCode': numberCountryCode,
        'countryIsoCode': numberCountry,
        'country': country,
        'location': location,
        'carrier': carrierName or providerId,
    }

    return numberObj
