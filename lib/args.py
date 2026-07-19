import argparse

parser = argparse.ArgumentParser(
    prog='phonia-id',
    usage='%(prog)s -n <number> [options]',
    epilog="Contoh: phonia-id -n 08123456789"
)

parser.add_argument('-n', '--number', type=str, help='Nomor HP target')
parser.add_argument('-i', '--input', type=str, help='File berisi daftar nomor')
parser.add_argument('-o', '--output', type=str, help='Output file')
parser.add_argument('--no-ansi', action='store_true', help='Nonaktifkan warna')
parser.add_argument('--info', action='store_true', help='Info tools')

args = parser.parse_known_args()[0]
