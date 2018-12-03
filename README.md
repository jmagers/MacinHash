# MacinHash
Convert MacOS plist password file to hash file for password crackers. Supports plist files from MacOS 10.8+. Can be run on any machine that supports Python.

## Dependencies
Python 3.5+

## Usage
Obtain the plist file located at /var/db/dslocal/nodes/Default/users/\<username\>.plist

Convert it to hash format **\<username\>:$ml$\<iterations\>$\<salt\>$\<entropy\>**
```
python3 machash.py <plist_file> <hash_file>
```

Use with a password cracker like hashcat or John the Ripper
```
hashcat -m 7100 --username <hash_file> <wordlist_file>
john <hash_file> -w <wordlist_file>
```
