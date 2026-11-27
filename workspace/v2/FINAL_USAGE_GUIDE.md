# 🦅 GHOSTHAWK v2.0 - Final Usage Guide for Linux

## 🎯 نظرة عامة

أداة **GHOSTHAWK v2.0** جاهزة الآن للاستخدام على نظام **Linux**!

---

## 📋 الملفات الموجودة في المجلد:

```
/workspace/v2/
├── cetj_security_scan_v2_linux.py    # ✅ Python script (الرئيسي)
├── ghosthawk.sh                       # ✅ Shell script wrapper
├── requirements.txt                   # ✅ مكتبات Python المطلوبة
├── README.md                          # ✅ التوثيق الرئيسي
├── INSTALLATION_GUIDE.md              # ✅ دليل التثبيت الشامل
├── QUICK_START.md                     # ✅ البدء السريع
├── GITHUB_UPLOAD_GUIDE.md             # ✅ رفع على GitHub
└── .gitignore                         # ✅ قواعد Git ignore
```

---

## 🚀 الخطوات النهائية قبل الاستخدام

### الخطوة 1: نقل الملفات إلى Linux

**الخيار أ: عبر SCP/SFTP:**
```bash
# من Windows (PowerShell)
scp -r /workspace/v2/* user@linux-server:/path/to/destination/

# أو من Linux
rsync -avz /workspace/v2/ user@linux-server:/path/to/destination/
```

**الخيار ب: عبر GitHub:**
1. رَفع الملفات إلى GitHub (راجع [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md))
2. Clone على Linux:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ghosthawk-v2.git
   cd ghosthawk-v2
   ```

**الخيار ج: عبر USB/Disk:**
1. انسخ المجلد `/workspace/v2/` إلى USB
2. نقله إلى Linux

---

### الخطوة 2: على نظام Linux

```bash
# 1. الانتقال إلى المجلد
cd /path/to/ghosthawk-v2

# 2. تثبيت المكتبات
pip3 install -r requirements.txt

# 3. جعل السكريبت قابل للتنفيذ
chmod +x ghosthawk.sh
chmod +x cetj_security_scan_v2_linux.py

# 4. عرض المساعدة
./ghosthawk.sh --help

# 5. تشغيل المسح!
./ghosthawk.sh --target https://example.com
```

---

## 📖 أوامر الاستخدام الشائعة

### 1. مسح بسيط:
```bash
./ghosthawk.sh -t https://cetj.edu.ly
```

### 2. مع Tor Proxy:
```bash
./ghosthawk.sh -t https://cetj.edu.ly -p tor -T 15
```

### 3. تقرير مخصص:
```bash
./ghosthawk.sh -t https://example.com -o report.json
```

### 4. وضع الصمت:
```bash
./ghosthawk.sh -t https://example.com -q
```

### 5. عرض المساعدة:
```bash
./ghosthawk.sh --help
```

**المخرجات:**
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

## 🔧 حل المشاكل الشائعة

### المشكلة 1: خطأ CRLF Line Endings

**الأعراض:**
```
zsh: ./ghosthawk.sh: bad interpreter: /bin/bash^M: no such file or directory
```

**الحل:**
```bash
sed -i 's/\r$//' ghosthawk.sh
sed -i 's/\r$//' cetj_security_scan_v2_linux.py

# أو استخدام dos2unix
dos2unix ghosthawk.sh
dos2unix cetj_security_scan_v2_linux.py
```

### المشكلة 2: مكتبات غير مثبتة

**الأعراض:**
```
ModuleNotFoundError: No module named 'requests'
```

**الحل:**
```bash
pip3 install requests beautifulsoup4
```

### المشكلة 3: Python3 غير موجود

**الأعراض:**
```
python3: command not found
```

**الحل:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### المشكلة 4: Tor Proxy غير يعمل

**الأعراض:**
```
Connection refused
```

**الحل:**
```bash
# تثبيت Tor
sudo apt install tor

# تشغيل Tor
sudo systemctl start tor

# أو استخدام SSH proxy بدلاً من ذلك
./ghosthawk.sh -t https://example.com -p ssh user@host:22
```

---

## 📊 النتائج المتوقعة

عند التشغيل ستحصل على:

1. ✅ **مسح شامل** للموقع المستهدف
2. ✅ **تقرير JSON** في الملف المحدد (أو `full_security_report.json`)
3. ✅ **تحذيرات** عن الثغرات المكتشفة
4. ✅ **إحصائيات** عن حالة الموقع الأمني

### مثال على التقرير:

```json
{
  "target": "https://cetj.edu.ly",
  "scan_time": "2024-01-15T10:30:00",
  "infrastructure": {
    "dns_records": {"status": "success", "ip": "192.168.1.1"},
    "ssl_certificate": {"valid": true, "days_remaining": 90},
    ...
  },
  "vulnerabilities": {...},
  ...
}
```

---

## 📁 الملفات الناتجة

```
full_security_report.json          # التقرير الكامل (JSON)
```

التقرير يحتوي على:
- ✅ Infrastructure Scan (DNS, SSL, HTTP Methods)
- ✅ Vulnerability Scan (Headers, CSRF, Mixed Content)
- ✅ SQL Injection Detection
- ✅ XSS Detection
- ✅ API Endpoint Discovery
- ✅ Cookie Security Analysis
- ✅ Rate Limiting Detection
- ✅ User Enumeration Detection
- ✅ Sensitive Files Scan

---

## 🎯 الخلاصة

**GHOSTHAWK v2.0 جاهز للاستخدام على Linux!**

### أوامر التشغيل السريعة:

```bash
# 1. عرض المساعدة
./ghosthawk.sh --help

# 2. مسح بسيط
./ghosthawk.sh -t https://example.com

# 3. مع Tor Proxy
./ghosthawk.sh -t https://cetj.edu.ly -p tor -T 15

# 4. تقرير مخصص
./ghosthawk.sh -t https://example.com -o report.json -q
```

---

## 📚 التوثيق الكامل

- [README.md](README.md) - التوثيق الرئيسي
- [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) - دليل التثبيت الشامل
- [QUICK_START.md](QUICK_START.md) - البدء السريع
- [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md) - رفع على GitHub

---

## 🎉 جاهز للاستخدام!

**GHOSTHAWK v2.0 - الباز الشبح جاهز للتنفيذ على Linux!**

```bash
./ghosthawk.sh --help  # ابدأ هنا!
```

---

**🦅 GHOSTHAWK v2.0 - Ready for Linux! 🚀**