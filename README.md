# Phonia-ID

**OSINT Nomor Telepon Indonesia**

Tool untuk scan nomor HP Indonesia — cek provider, lokasi, WhatsApp, jejak sosial media, dan Google Maps.

---

## Fitur

| Fitur | Keterangan |
|-------|-----------|
| 📱 **Info Nomor** | Negara, provider, tipe (Prabayar/Pascabayar), timezone |
| 📍 **Wilayah** | Deteksi lokasi via prefix/kode area |
| 🏢 **Provider ID** | Database lengkap provider Indonesia (Telkomsel, Indosat, XL, Tri, Smartfren, Axis, By.U, Bolt) |
| 💬 **WhatsApp** | Cek nomor terdaftar WhatsApp atau tidak |
| 🌐 **Sosial Media** | Google dork: Facebook, Instagram, Twitter, TikTok, LinkedIn, Tokopedia, Shopee, Kaskus |
| 🗺️ **Google Maps** | Link Google Maps dari data yang ditemukan |
| 📋 **Bulk Scan** | Scan banyak nomor dari file |

## Instalasi

```bash
git clone https://github.com/clickmamaheti-prog/phonia-id.git
cd phonia-id
pip install -r requirements.txt
```

## Penggunaan

```bash
# Scan satu nomor
python3 phonia-id.py -n 08123456789

# Scan dari file
python3 phonia-id.py -i daftar_nomor.txt

# Simpan hasil
python3 phonia-id.py -n 08123456789 -o hasil.txt
```

## Contoh Output

```
📱 Nomor       : +62 8XX-XXXX-XXXX
🌍 Negara      : Indonesia (ID)
📍 Wilayah     : Axis (Nasional)
🏢 Provider    : AXIS
📋 Tipe        : Prabayar
🕐 Timezone    : Asia/Jakarta

✅ WhatsApp: Tersedia di wa.me/628XXXXXXXXXX
```

## Sumber Data

- **Google Dork**: Pencarian sosial media via Google
- **Numverify**: Informasi nomor internasional
- **Database Prefix**: Database provider & kode area Indonesia
- **WhatsApp**: wa.me API

## Catatan

- ⚠️ Untuk **edukasi dan keamanan** saja
- 📱 Nomor HP **tidak bisa** dilacak lokasi pastinya (beda dengan nomor rumah)
- 🔒 Privasi tergantung seberapa banyak data yang bocor di internet

---

**DevCult XII** — Crafting Premium AI Experiences
