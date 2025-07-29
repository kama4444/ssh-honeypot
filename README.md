 Brute-Force SSH Honeypot

**SSH honeypot** designed to log brute-force login attempts on port 22. Built with Python, it simulates a real SSH server to lure attackers, record their login credential.
Between June and July 2024, this honeypot was deployed in a home lab environment, exposing port 22 to the public internet. Within the first 5 days, it captured over 200 unauthorized login attempts from various global IP addresses.

Purpose

1)Helps understand how attackers operate
- Logs credentials
- Provides data for brute force analysis

Runs on port 22 using Python and Paramiko


Setup 

Make sure to install libraries and `paramiko` is installed.
Create a log file with mkdir data. This is where logs will be kept. data/
run the python file with brute force using sudo command.
and open the log file with command cat.
