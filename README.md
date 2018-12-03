# MacinHash
Convert MacOS plist password file to hash file for Hashcat. Supports plist files from MacOS 10.8+. Can be run on any machine that supports Python.

## Dependencies
Python 3.5+

## Usage
Obtain the plist file located at /var/db/dslocal/nodes/Default/users/<username>.plist

Convert it to hashcat format
```
python3 machash.py <plist_file> <hashcat_file>
```

Use with hashcat
```
hashcat -m 7100 <hashcat_file> <wordlist_file>
```
