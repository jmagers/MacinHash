#!/usr/bin/env python3

import plistlib
import sys

# Check number of args
if not 2 <= len(sys.argv) <= 3:
    sys.exit("Must provide 1 or 2 arguments!")

# Load plist file
PLIST_FILE_NAME = sys.argv[1]
plist = None
try:
    with open(PLIST_FILE_NAME, 'rb') as pfile:
        plist = plistlib.load(pfile)
except:
    sys.exit("Could not load plist file!")

# Set file to store results
try:
    RESULT_FILE = open(sys.argv[2], 'w')
except IndexError:
    RESULT_FILE = sys.stdout
except:
    sys.exit("Could not open results file!")

# Collect hash data
shadow_hash_data = plistlib.loads(plist['ShadowHashData'][0])
data = shadow_hash_data['SALTED-SHA512-PBKDF2']
iterations = str(data['iterations'])
salt = data['salt'].hex()
entropy = data['entropy'].hex()

# Format and output hash data
formatted_hash = '$'.join(['$ml', iterations, salt, entropy])
print(formatted_hash, file=RESULT_FILE)

# Cleanup
RESULT_FILE.close()
