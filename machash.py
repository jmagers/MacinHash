#!/usr/bin/env python3

# This software is Copyright (c) 2017 Jake Magers <jmagers12 at gmail.com>,
# and it is hereby released to the general public under the following terms:
# Redistribution and use in source and binary forms, with or without
# modification, are permitted.

import argparse
import plistlib
import sys

HASH_TYPE = 'SALTED-SHA512-PBKDF2'

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
try:
    shadow_hash_data = plistlib.loads(plist['ShadowHashData'][0])
except (KeyError, IndexError):
    sys.exit("ShadowHashData not found in plist file!")
except plistlib.InvalidFileException:
    sys.exit("Could not load ShadowHashData from plist file!")
try:
    data = shadow_hash_data[HASH_TYPE]
except KeyError:
    sys.exit("ShadowHashData is not of type '%s' and therefore incompatible!"
             % HASH_TYPE)
iterations = str(data['iterations'])
salt = data['salt'].hex()
entropy = data['entropy'].hex()

# Format and output hash data
formatted_hash = '$'.join(['$ml', iterations, salt, entropy])
print(formatted_hash, file=args.hashfile)
