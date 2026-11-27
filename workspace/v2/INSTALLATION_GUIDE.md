# 🦅 GHOSTHAWK v2.0 - Linux Installation & Usage Guide

## 📋 Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Advanced Features](#advanced-features)

---

## Installation

### 1. Clone or Download the Project

```bash
# Option 1: From GitHub
git clone https://github.com/YOUR_USERNAME/ghosthawk-v2.git
cd ghosthawk-v2

# Option 2: Manual download
# Upload the /workspace/v2 folder to your Linux system
```

### 2. Install Dependencies

```bash
# Method 1: Using pip3 (Recommended)
pip3 install -r requirements.txt

# Method 2: Install individually
pip3 install requests beautifulsoup4

# Verify installation
python3 -c "import requests; import bs4; print('✅ All dependencies installed!')"
```

### 3. Make Scripts Executable

```bash
chmod +x ghosthawk.sh
chmod +x cetj_security_scan_v2_linux.py
```

---

## Quick Start

### Basic Scan

```bash
python3 cetj_security_scan_v2_linux.py --target https://example.com
```

### Using the Shell Script (Recommended)

```bash
./ghosthawk.sh --target https://example.com
```

---

## Usage Examples

### 1. Basic Scan

```bash
# Simple scan with default settings
python3 cetj_security_scan_v2_linux.py --target https://cetj.edu.ly

# Or using shell script
./ghosthawk.sh -t https://cetj.edu.ly
```

### 2. With Tor Proxy

```bash
# Install Tor first (if not installed)
sudo apt install tor

# Start Tor service
sudo systemctl start tor

# Scan with Tor proxy
python3 cetj_security_scan_v2_linux.py \
  --target https://cetj.edu.ly \
  --proxy tor \
  --timeout 15

# Or using shell script
./ghosthawk.sh -t https://cetj.edu.ly -p tor -T 15
```

### 3. Custom Output File

```bash
python3 cetj_security_scan_v2_linux.py \
  --target https://example.com \
  --output my_report.json
```

### 4. Quiet Mode (Less Output)

```bash
python3 cetj_security_scan_v2_linux.py \
  --target https://example.com \
  --quiet
```

### 5. All Options Combined

```bash
python3 cetj_security_scan_v2_linux.py \
  --target https://cetj.edu.ly \
  --proxy tor \
  --timeout 20 \
  --output detailed_report.json \
  --quiet
```

---

## Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--target` | `-t` | Target URL to scan | `https://cetj.edu.ly` |
| `--proxy` | `-p` | Proxy type (tor/ssh/http/https) | `false` |
| `--timeout` | `-T` | Request timeout in seconds | `10` |
| `--output` | `-o` | Output file for report | `full_security_report.json` |
| `--quiet` | `-q` | Quiet mode (less output) | `false` |
| `--help` | `-h` | Show help message | - |

---

## Shell Script Usage

### Basic Usage

```bash
./ghosthawk.sh --target https://example.com
```

### Short Options

```bash
./ghosthawk.sh -t https://example.com -p tor -T 15 -o report.json
```

### Help Message

```bash
./ghosthawk.sh --help
```

**Output:**
```
=======================================================================
🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner
=======================================================================

📋 Usage:
   ./ghosthawk.sh [OPTIONS]

🎯 Options:
   --target, -t     Target URL (default: https://cetj.edu.ly)
   --proxy, -p      Proxy type: tor/ssh/http/https (default: none)
   --timeout, -T    Request timeout in seconds (default: 10)
   --output, -o     Output file for report (default: full_security_report.json)
   --quiet, -q      Quiet mode - only show critical results
   --help, -h       Show this help message

📝 Examples:
   ./ghosthawk.sh --target https://example.com
   ./ghosthawk.sh -t https://example.com -p tor -T 15 -o report.json
   ./ghosthawk.sh --target https://example.com --quiet

=======================================================================
```

---

## Troubleshooting

### 1. CRLF Line Endings Error

**Error:**
```
zsh: ./ghosthawk.sh: bad interpreter: /bin/bash^M: no such file or directory
```

**Solution:**
```bash
# Convert Windows line endings to Unix
sed -i 's/\r$//' ghosthawk.sh
sed -i 's/\r$//' cetj_security_scan_v2_linux.py

# Or use dos2unix (if installed)
dos2unix ghosthawk.sh
dos2unix cetj_security_scan_v2_linux.py
```

### 2. Missing Dependencies

**Error:**
```
ModuleNotFoundError: No module named 'requests'
```

**Solution:**
```bash
pip3 install requests beautifulsoup4
```

### 3. Python3 Not Found

**Error:**
```
python3: command not found
```

**Solution:**
```bash
# Install Python3
sudo apt update
sudo apt install python3 python3-pip

# Verify installation
python3 --version
```

### 4. Tor Proxy Not Working

**Error:**
```
Connection refused
```

**Solution:**
```bash
# Check if Tor is running
sudo systemctl status tor

# Start Tor service
sudo systemctl start tor

# Or use SSH proxy instead
./ghosthawk.sh -t https://example.com -p ssh user@host:22
```

### 5. SSL Certificate Error

**Error:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Solution:**
```bash
# Update system certificates
sudo apt update && sudo apt install ca-certificates

# Or use --insecure flag (not recommended for production)
python3 cetj_security_scan_v2_linux.py --target https://example.com --insecure
```

---

## Advanced Features

### 1. Scheduled Scans (Cron Job)

Create a cron job to scan daily:

```bash
# Edit crontab
crontab -e

# Add this line for daily scan at 2 AM
0 2 * * * /path/to/ghosthawk.sh --target https://example.com >> /var/log/ghosthawk_scan.log 2>&1
```

### 2. Parallel Scans

Scan multiple targets:

```bash
#!/bin/bash
# parallel_scans.sh

TARGETS=(
    "https://target1.com"
    "https://target2.com"
    "https://target3.com"
)

for target in "${TARGETS[@]}"; do
    echo "Scanning: $target"
    python3 cetj_security_scan_v2_linux.py \
        --target "$target" \
        --output "$(basename "$target" .com).json" &
done

wait
echo "✅ All scans completed!"
```

### 3. Generate Report Summary

Create a summary script:

```bash
#!/bin/bash
# generate_summary.sh

python3 -c "
import json
with open('full_security_report.json', 'r') as f:
    report = json.load(f)

print('\n' + '='*60)
print('📊 SCAN SUMMARY')
print('='*60)
print(f'Target: {report[\"target\"]}')
print(f'Scan Time: {report[\"scan_time\"]}')
print('='*60 + '\n')
"
```

### 4. API Rate Limiting

For high-frequency scanning, add delays:

```python
import time
import random

# Add random delay between requests (1-3 seconds)
time.sleep(random.uniform(1, 3))
```

---

## Security Best Practices

### 1. Never Share Credentials

⚠️ **Important:** Remove any credentials from the report before sharing:

```bash
# Remove sensitive data from JSON report
python3 -c "
import json
import re

with open('full_security_report.json', 'r') as f:
    content = f.read()

# Remove passwords and tokens
content = re.sub(r'password\s*:\s*\S+', 'password: [REDACTED]', content)
content = re.sub(r'token\s*:\s*\S+', 'token: [REDACTED]', content)

with open('full_security_report.json', 'w') as f:
    f.write(content)
"
```

### 2. Use Virtual Environment

```bash
# Create virtual environment
python3 -m venv ghosthawk_venv

# Activate it
source ghosthawk_venv/bin/activate

# Install dependencies
pip install requests beautifulsoup4

# Run scanner
python3 cetj_security_scan_v2_linux.py --target https://example.com
```

### 3. Secure the Report File

```bash
# Set read-only permissions
chmod 444 full_security_report.json

# Or encrypt sensitive reports
openssl enc -aes-256-cbc -salt -in full_security_report.json -out full_security_report.json.enc -pass pass:your_password
```

---

## Performance Tips

### 1. Increase Timeout for Slow Connections

```bash
python3 cetj_security_scan_v2_linux.py --target https://example.com --timeout 30
```

### 2. Use Multiple Proxies

```bash
# Rotate between multiple proxies
python3 -c "
import random
proxies = ['tor', 'ssh://user@host1:22', 'http://proxy1:8080']
print(random.choice(proxies))
" | xargs -I {} ./ghosthawk.sh -t https://example.com -p {}
```

### 3. Batch Processing

```bash
#!/bin/bash
# batch_scan.sh

TARGETS_FILE="targets.txt"  # One URL per line

while read target; do
    echo "Scanning: $target"
    python3 cetj_security_scan_v2_linux.py \
        --target "$target" \
        --output "$(basename "$target" .com).json" &
done < "$TARGETS_FILE"

wait
echo "✅ Batch scan completed!"
```

---

## File Structure

```
/workspace/v2/
├── cetj_security_scan_v2_linux.py    # Main Python scanner (Linux optimized)
├── ghosthawk.sh                       # Shell script wrapper
├── requirements.txt                   # Python dependencies
├── README.md                          # Documentation
└── .gitignore                         # Git ignore rules
```

---

## License

This project is open source and available for educational purposes.

---

## Support

For issues or questions, please check:
- [README.md](README.md) for documentation
- [Troubleshooting section](#troubleshooting) for common errors

---

**🦅 GHOSTHAWK v2.0 - Ready for Linux! 🚀**