# 🦅 GHOSTHAWK v2.0 - GitHub Upload Guide

## 📋 Table of Contents
- [Upload to GitHub](#upload-to-github)
- [Local Testing](#local-testing)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)

---

## Upload to GitHub

### Option 1: Create New Repository

```bash
# 1. Navigate to project directory
cd /workspace/v2

# 2. Initialize Git repository (if not already initialized)
git init

# 3. Add all files
git add .

# 4. Commit changes
git commit -m "Initial commit: GHOSTHAWK v2.0 - Linux Optimized Security Scanner"

# 5. Create new repository on GitHub
# Go to: https://github.com/new
# Repository name: ghosthawk-v2
# Description: GHOSTHAWK v2.0 - Linux Optimized Security Scanner

# 6. Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/ghosthawk-v2.git
git branch -M main
git push -u origin main

# Or push to a specific branch
git push origin linux-port-v2
```

### Option 2: Upload via GitHub Web Interface

1. Go to: https://github.com/new
2. Fill in repository details:
   - **Repository name**: `ghosthawk-v2`
   - **Description**: `GHOSTHAWK v2.0 - Linux Optimized Security Scanner`
   - **Visibility**: Public or Private (your choice)
3. Click "Create repository"
4. Drag and drop files from `/workspace/v2/` to the upload area
5. Or copy files manually:
   - `cetj_security_scan_v2_linux.py`
   - `ghosthawk.sh`
   - `requirements.txt`
   - `README.md`
   - `INSTALLATION_GUIDE.md`
   - `QUICK_START.md`
   - `.gitignore`

### Option 3: Create from Command Line (GitHub CLI)

```bash
# Install GitHub CLI (if not installed)
# Ubuntu/Debian:
sudo apt install gh

# Login to GitHub
gh auth login

# Create new repository
gh repo create ghosthawk-v2 \
  --public \
  --description "GHOSTHAWK v2.0 - Linux Optimized Security Scanner"

# Navigate to repository
cd ghosthawk-v2

# Add and push files
git add .
git commit -m "GHOSTHAWK v2.0 - Linux Optimized with all fixes"
git push origin main
```

---

## Local Testing (Before Upload)

### 1. Verify All Files

```bash
cd /workspace/v2

# List all files
ls -la

# Expected files:
# ├── cetj_security_scan_v2_linux.py    ✅ Main Python script
# ├── ghosthawk.sh                       ✅ Shell script wrapper
# ├── requirements.txt                   ✅ Dependencies
# ├── README.md                          ✅ Documentation
# ├── INSTALLATION_GUIDE.md              ✅ Installation guide
# ├── QUICK_START.md                     ✅ Quick start guide
# └── .gitignore                         ✅ Git ignore rules
```

### 2. Test Python Script

```bash
# Check if script is executable
python3 cetj_security_scan_v2_linux.py --help

# Expected output:
# usage: cetj_security_scan_v2_linux.py [-h] [--target TARGET] [--proxy PROXY] ...
# 🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner
```

### 3. Test Shell Script

```bash
# Make it executable (if not already)
chmod +x ghosthawk.sh

# Test help command
./ghosthawk.sh --help

# Expected output:
# =======================================================================
# 🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner
# =======================================================================
# 📋 Usage: $0 [OPTIONS]
# ...
```

### 4. Verify Dependencies

```bash
pip3 install -r requirements.txt

# Test imports
python3 -c "import requests; import bs4; print('✅ All dependencies installed!')"
```

### 5. Fix CRLF Line Endings (if needed)

```bash
sed -i 's/\r$//' cetj_security_scan_v2_linux.py
sed -i 's/\r$//' ghosthawk.sh

# Verify fix
file cetj_security_scan_v2_linux.py
# Should show: ASCII text, with very long lines (not CRLF)
```

---

## File Structure

### Final Repository Structure:

```
ghosthawk-v2/
├── cetj_security_scan_v2_linux.py    # ✅ Main Python script (Linux optimized)
├── ghosthawk.sh                       # ✅ Shell script wrapper
├── requirements.txt                   # ✅ Python dependencies
├── README.md                          # ✅ Main documentation
├── INSTALLATION_GUIDE.md              # ✅ Detailed installation guide
├── QUICK_START.md                     # ✅ Quick start guide
└── .gitignore                         # ✅ Git ignore rules

Total files: 7
Total size: ~50KB (excluding reports)
```

### File Descriptions:

| File | Purpose | Size |
|------|---------|------|
| `cetj_security_scan_v2_linux.py` | Main Python scanner | ~3,500 lines |
| `ghosthawk.sh` | Shell wrapper script | ~130 lines |
| `requirements.txt` | Python dependencies | 2 lines |
| `README.md` | Main documentation | ~291 lines |
| `INSTALLATION_GUIDE.md` | Installation guide | ~463 lines |
| `QUICK_START.md` | Quick start guide | ~112 lines |
| `.gitignore` | Git ignore rules | 33 lines |

---

## Troubleshooting

### Issue 1: Git Not Installed

```bash
sudo apt update
sudo apt install git
```

### Issue 2: Python3 Not Found

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Issue 3: CRLF Line Endings Error

```bash
# Convert Windows line endings to Unix
sed -i 's/\r$//' cetj_security_scan_v2_linux.py
sed -i 's/\r$//' ghosthawk.sh

# Or use dos2unix (if installed)
dos2unix cetj_security_scan_v2_linux.py
dos2unix ghosthawk.sh
```

### Issue 4: Missing Dependencies

```bash
pip3 install requests beautifulsoup4

# Or install from requirements.txt
pip3 install -r requirements.txt
```

### Issue 5: Permission Denied

```bash
chmod +x cetj_security_scan_v2_linux.py
chmod +x ghosthawk.sh
```

### Issue 6: Git Push Fails

```bash
# Check remote URL
git remote -v

# Add remote if needed
git remote add origin https://github.com/YOUR_USERNAME/ghosthawk-v2.git

# Set upstream branch
git push -u origin main

# Or push to specific branch
git push origin linux-port-v2
```

---

## Verification Checklist

Before uploading, verify:

- [ ] All 7 files are present
- [ ] Python script runs with `--help`
- [ ] Shell script runs with `--help`
- [ ] CRLF line endings are fixed
- [ ] Dependencies can be installed
- [ ] Git is installed and configured
- [ ] Remote repository is created on GitHub

---

## Post-Upload Actions

### 1. Create Release

```bash
# Tag the release
git tag -a v2.0 -m "GHOSTHAWK v2.0 Release"
git push origin v2.0
```

### 2. Add to README (GitHub)

Edit `README.md` on GitHub and add:
- Installation instructions
- Usage examples
- Screenshots (if available)
- License information

### 3. Create Wiki

Create a GitHub Wiki with:
- Detailed documentation
- Troubleshooting guide
- FAQ section
- Contributing guidelines

---

## Security Notes

⚠️ **Important:**
- Never commit sensitive data (API keys, passwords)
- Use `.gitignore` to exclude report files
- Keep repository private if containing sensitive code
- Add security policy in repository settings

---

## License

This project is open source and available for educational purposes.

---

**🦅 GHOSTHAWK v2.0 - Ready for GitHub! 🚀**