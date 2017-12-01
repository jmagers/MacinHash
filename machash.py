#!/usr/bin/env python3

import argparse
import plistlib
import sys

# Arguments
parser = argparse.ArgumentParser(description='Convert Mac plist password file '
                                 'to hash file')
parser.add_argument('plistfile',
                    type=argparse.FileType('rb'),
                    help='plist file to convert to hash')
parser.add_argument('hashfile',
                    type=argparse.FileType('w'),
                    nargs='?',
                    default='-',
                    help='file to store resulting hash')
args = parser.parse_args()

# Load plist file
try:
    plist = plistlib.load(args.plistfile)
except plistlib.InvalidFileException:
    sys.exit("Could not parse plist file!")

# Collect hash data
shadow_hash_data = plistlib.loads(plist['ShadowHashData'][0])
data = shadow_hash_data['SALTED-SHA512-PBKDF2']
iterations = str(data['iterations'])
salt = data['salt'].hex()
entropy = data['entropy'].hex()

# Format and output hash data
formatted_hash = '$'.join(['$ml', iterations, salt, entropy])
print(formatted_hash, file=args.hashfile)
