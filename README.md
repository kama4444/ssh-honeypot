# ssh-honeypot
# Brute-Force SSH Attack Honeypot

## Project Overview
This project deploys a basic SSH honeypot on a Linux system to analyze brute force attacks. It exposes port 22 to the public internet to attract attackers, and logs their behavior.



## Key Feature
- Open port 22 using `ufw`
- Basic logging with `Cowrie` or custom Python script
- Captures attacker behavior (file uploads, reverse shell attempts)
- Analysis of IPs, credentials, and attack patterns

## Folder Structure
- `src/`: Python honeypot server code (optional if not using Cowrie)
- `data/`: Raw logs of login attempts
- `scripts/`: Tools for analyzing attacker data
- `docs/`: Setup and usage documentation
- `images/`: Architecture diagrams and screenshots

## License
MIT License
