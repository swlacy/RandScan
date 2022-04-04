#!/usr/bin/env python3

"""DOCSTRING: This script queries internetdb.shodan.io with random IP addresses.
Intended use: data collection and research. Outputs in YAML."""

__author__ = "Sid Lacy"
__copyright__ = "MIT"

import sys, random, requests, json

# Input validation
if len(sys.argv) != 2:
    print("Usage: ./rand_scan.py <iterations>")
    exit()

# Generate, query for <arg> times
for i in range(int(sys.argv[1])):
    ip = []
    for j in range(4):
        ip.append(random.randint(0, 255))

    # Filter out private addresses
    if (ip[0] == 10) or (ip[0] == 172 and ip[1] in range(16, 32)) or (ip[0] == 192 and ip[1] == 168):
        i -= 1
        continue

    # Grab data on address from Shodan
    ip = f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}'
    r = requests.get(f'https://internetdb.shodan.io/{ip}')
    
    # Only print if there is important info
    if r.status_code == 200:
        jdata = json.loads(r.text)
        print(f'({i + 1}) https://www.shodan.io/host/{ip}:')
        if len(jdata['tags']) > 0:
            print('    Tag(s):\n    - ' +'\n    - '.join(str(item) for item in jdata['tags']))
        if len(jdata['hostnames']) > 0:
            print('    Host(s):\n    - ' +'\n    - '.join(str(item) for item in jdata['hostnames']))
        if len(jdata['cpes']) > 0:
            print('    CPE(s):\n    - ' +'\n    - '.join(str(item) for item in jdata['cpes']))
        if len(jdata['vulns']) > 0:
            print('    CVE(s):\n    - ' +'\n    - '.join(str(item) for item in jdata['vulns']))
        if len(jdata['ports']) > 0:
            print('    Port(s):\n    - ' +'\n    - '.join(str(item) for item in jdata['ports']) + '\n')
