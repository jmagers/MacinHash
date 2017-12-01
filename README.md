# MacinHash
Convert MacOS plist password file to hash file for Hashcat. Supports MacOS 10.8+.

## Dependencies
Python 3.5+

## Usage
Obtain the plist file located in /var/db/dslocal/nodes/Default/users/

Convert it to hashcat format with:
```
python3 machash.py <plist_file> <hashcat_file>
```
