# RandScan
Script that queries internetdb.shodan.io with random IP addresses. Intended use: data collection and research. Outputs in YAML. No API key needed.

Just for fun and education; please no malicious use.

## Usage
`./rand_scan.py ${iterations}` where `${iterations}` is the number of IP addresses to generate and query data on. Example:

```
$ ./rand_scan.py 100

(14) https://www.shodan.io/host/159.89.120.42:
    Tag(s):
    - cloud
    Host(s):
    - eff-2004.ca.cap-systems.org
    - eff.ca.cap-systems.org
    CPE(s):
    - cpe:/a:apache:http_server:2.4.41
    - cpe:/a:jquery:jquery
    Port(s):
    - 80
    - 443

(23) https://www.shodan.io/host/211.225.164.54:
    Port(s):
    - 7547

(58) https://www.shodan.io/host/124.66.14.54:
    CPE(s):
    - cpe:/a:openbsd:openssh:7.4
    CVE(s):
    - CVE-2017-15906
    - CVE-2018-15919
    Port(s):
    - 3389

(99) https://www.shodan.io/host/125.24.203.87:
    Host(s):
    - node-145z.pool-125-24.dynamic.totinternet.net
    Port(s):
    - 443
    - 7547

$
```

Note that empty sets are excluded.

PRs welcome.