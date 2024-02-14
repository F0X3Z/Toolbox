# Toolbox

This toolbox provides a collection of tools for various tasks. Below are instructions for setup and usage of each tool.

## Installation

To get started, clone this repository:

```bash
git clone https://github.com/F0X3Z/Toolbox.git
```

Additionally, ensure you have the following dependencies installed:

Zed Attack Proxy
Python 3

Install Python dependencies using pip:

```bash
apt-get install zaproxy python3
pip install requests python-owasp-zap-v2.4 selenium python-nmap
```
## PYZAP
This tool will help you run a vulnerbility scan against a website and creating a vulnerbility-report.

Start your headless Zed Attack Proxy server:
```bash
zaproxy -daemon
```

Change your api-key inside pyzap.py and url if you are not running it on your localhost.
You can find you api-key here: ~/.ZAP/config.xml
```bash
python3 pyzap.py https://example.com
```

## NMAP
This tool uses Nmap to create a list of hosts on a ip-range.

Adjust the network range according to your requirements and run the scan:

```bash
python3 scan.py
```

## DEHASHER SHA1 & MD5
This tool helps you dehash SHA1 & MD5 hashes.

Execute the dehasher script:

```bash
python3 dehasher.py
```

## FILTER
This script will help you separate combos from the Naz.Api leak.

```bash
python3 filter.py
```

## WEB SHELL

```bash
usage = Usage: python3 exploit.py HOST PORT COMMAND

Ex: python3 exploit.py 10.0.0.1 10000 id

```

## BRUTE FORCE

Using bruteforce

```bash
bruteforce --url http://example.com/login --user username --max-length 4 --chars abc123
bruteforce --url http://localhost:3000/auth/login --user user@example.com --max-length 8 --chars adoprsw
```

Using bfselenium
```bash
bfselenium --url http://localhost:3000 --user user@example.com --max-length 8 --chars adoprsw
```
