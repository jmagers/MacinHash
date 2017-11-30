# MacinHash
Convert MacOS plist password file to simple hash file for Hashcat. Tested on MacOS 10.13.

## Usage
Obtain the plist file located in /var/db/dslocal/nodes/Default/users/

Convert it to hashcat format with:
```
python3 machash.py <plist_file> <hashcat_file>
```
