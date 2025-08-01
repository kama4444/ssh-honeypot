Brute-Force SSH Honeypot
=====
A Python-based SSH honeypot that simulates a real SSH server to log brute-force login attempts on port 22.

Deployment Info:

• Deployed: June–July 2024 (home lab)
• Port 22 was exposed to the public internet
• Logged 200+ unauthorized login attempts in the first 5 days
• Captured global IPs, usernames, and passwords

Purpose:

• Understand how brute-force attackers behave
• Log all attempted SSH credentials and source IPs
• Analyze patterns in attack frequency and methods

Tools
-------------
• Language: Python
• Library: Paramiko

How It Works:
-------------
• Listens on port 22 (SSH)
• Accepts any login attempt (does not validate)
• Logs the following to /data/log.txt:
    - Username
    - Password
    - Source IP
    - Timestamp

Setup instructions:

1. Install dependencies:
    pip install paramiko

2. Create log directory:
    mkdir data

3. Run the honeypot (requires sudo for port 22):
    sudo python3 honeypot.py

4. View logs:
    cat data/log.txt
