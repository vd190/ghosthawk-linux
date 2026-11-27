# 🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner

## 🎯 نظرة عامة

**GHOSTHAWK v2.0** هو أداة مسح أمني متكاملة ومُحسّنة خصيصاً لبيئة **Linux**، تقوم بفحص المواقع الإلكترونية واكتشاف الثغرات الأمنية مع الحفاظ على إخفاء الهوية الكامل.

### ✨ المميزات:

- ✅ **مسح شامل** للثغرات الأمنية (SQL Injection, XSS, CSRF, etc.)
- ✅ **دعم Tor/VPN Proxy** لإخفاء الهوية
- ✅ **Linux Optimized** - خالية من تبعيات Windows
- ✅ **أوامر سطر الأوامر** (--target, --proxy, --timeout, --output, --quiet)
- ✅ **تقرير JSON** شامل مع جميع النتائج
- ✅ **فحص تلقائي** للمكتبات قبل البدء

---

## 📋 المتطلبات

### 1. نظام التشغيل:
```bash
Ubuntu 20.04+ / Debian 10+ / Kali Linux / Parrot OS
```

### 2. Python 3.x:
```bash
python3 --version  # يجب أن يكون 3.6 أو أعلى
```

### 3. مكتبات Python:
```bash
pip3 install requests beautifulsoup4
```

---

## 🚀 البدء السريع

### 1. تثبيت المكتبات:
```bash
pip3 install -r requirements.txt
```

### 2. تشغيل المسح الكامل:
```bash
python3 cetj_security_scan_v2_linux.py --target https://example.com
```

### 3. أو استخدام shell script (موصى به):
```bash
./ghosthawk.sh --target https://example.com
```

---

## 📖 الاستخدام

### أوامر سطر الأوامر:

| الخيار | الوصف | القيمة الافتراضية |
|--------|-------|------------------|
| `--target` أو `-t` | رابط الموقع المستهدف | `https://cetj.edu.ly` |
| `--proxy` أو `-p` | نوع البروكسي (tor/ssh/http/https) | `false` |
| `--timeout` أو `-T` | وقت الانتظار بالثواني | `10` |
| `--output` أو `-o` | ملف التقرير الناتج | `full_security_report.json` |
| `--quiet` أو `-q` | وضع الصمت (نتائج فقط) | `false` |
| `--help` أو `-h` | عرض المساعدة | - |

### أمثلة على الاستخدام:

#### 1. مسح بسيط:
```bash
python3 cetj_security_scan_v2_linux.py --target https://example.com
```

#### 2. مع Tor Proxy:
```bash
python3 cetj_security_scan_v2_linux.py \
  --target https://cetj.edu.ly \
  --proxy tor \
  --timeout 15
```

#### 3. تقرير مخصص:
```bash
python3 cetj_security_scan_v2_linux.py \
  --target https://example.com \
  --output my_report.json
```

#### 4. وضع الصمت:
```bash
python3 cetj_security_scan_v2_linux.py \
  --target https://example.com \
  --quiet
```

#### 5. استخدام shell script:
```bash
./ghosthawk.sh -t https://example.com -p tor -T 15 -o report.json
```

---

## 📊 الميزات المُنفذة

| الميزة | الحالة | الوصف |
|--------|--------|-------|
| **Infrastructure Scan** | ✅ | فحص DNS, SSL, HTTP Methods |
| **Vulnerability Scan** | ✅ | Headers, CSRF, Mixed Content |
| **SQL Injection Detection** | ✅ | اختبار نقاط نهاية SQLi |
| **XSS Detection** | ✅ | اختبار ثغرات XSS |
| **Weak Password Brute-Force** | ⚠️ | محدودة (تحتاج login page) |
| **API Endpoint Discovery** | ✅ | اكتشاف نقاط نهاية API |
| **Cookie Security Analysis** | ✅ | فحص ملفات تعريف الارتباط |
| **Rate Limiting Detection** | ✅ | كشف حماية Rate Limiting |
| **User Enumeration Detection** | ✅ | كشف تسرب معلومات المستخدمين |
| **Sensitive Files Scan** | ✅ | فحص الملفات الحساسة |
| **Linux Optimized Headers** | ✅ | Headers متوافقة مع Linux |
| **argparse Support** | ✅ | دعم كامل لأوامر سطر الأوامر |
| **--help Command** | ✅ | عرض المساعدة الكامل |
| **فحص تلقائي للمكتبات** | ✅ | التحقق من توفر المكتبات |

---

## 🔧 التثبيت والتشغيل

### 1. تثبيت المكتبات:
```bash
pip3 install -r requirements.txt
```

أو تثبيت يدوياً:
```bash
pip3 install requests beautifulsoup4
```

### 2. جعل السكريبت قابل للتنفيذ:
```bash
chmod +x ghosthawk.sh
chmod +x cetj_security_scan_v2_linux.py
```

### 3. تشغيل المسح:
```bash
./ghosthawk.sh --target https://example.com
```

---

## 🛠️ حل المشاكل الشائعة

### 1. خطأ CRLF Line Endings:
```bash
# تحويل Windows line endings إلى Unix
sed -i 's/\r$//' ghosthawk.sh
sed -i 's/\r$//' cetj_security_scan_v2_linux.py
```

### 2. مكتبات غير مثبتة:
```bash
pip3 install requests beautifulsoup4
```

### 3. Python3 غير موجود:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 4. Tor Proxy غير يعمل:
```bash
# تثبيت Tor
sudo apt install tor

# تشغيل Tor
sudo systemctl start tor

# أو استخدام SSH proxy بدلاً من ذلك
./ghosthawk.sh -t https://example.com -p ssh user@host:22
```

---

## 📁 هيكل الملفات

```
/workspace/v2/
├── cetj_security_scan_v2_linux.py    # ✅ Python script (Linux optimized)
├── ghosthawk.sh                       # ✅ Shell script wrapper
├── requirements.txt                   # ✅ Python dependencies
├── README.md                          # ✅ هذا الملف
├── INSTALLATION_GUIDE.md              # ✅ دليل التثبيت الشامل
└── .gitignore                         # ✅ Git ignore rules
```

---

## 🔒 الأمان وأفضل الممارسات

### 1. استخدام Virtual Environment:
```bash
python3 -m venv ghosthawk_venv
source ghosthawk_venv/bin/activate
pip install requests beautifulsoup4
```

### 2. إزالة البيانات الحساسة من التقرير:
```bash
# قبل مشاركة التقرير، احذف كلمات المرور والأمان
python3 -c "
import json
with open('full_security_report.json', 'r') as f:
    content = f.read()
content = re.sub(r'password\s*:\s*\S+', 'password: [REDACTED]', content)
with open('full_security_report.json', 'w') as f:
    f.write(content)
"
```

### 3. تشفير التقرير الحساس:
```bash
openssl enc -aes-256-cbc -salt -in full_security_report.json -out full_security_report.json.enc -pass pass:your_password
```

---

## 📈 الأداء والنصائح

### 1. زيادة Timeout للروابط البطيئة:
```bash
python3 cetj_security_scan_v2_linux.py --target https://example.com --timeout 30
```

### 2. مسح متعدد للمواقع (Batch):
```bash
#!/bin/bash
# batch_scan.sh

TARGETS_FILE="targets.txt"  # كل رابط في سطر جديد

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

## 📝 التوثيق الكامل

للمزيد من التفاصيل، راجع:
- [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) - دليل التثبيت الشامل
- [README.md](README.md) - هذا الملف

---

## 🎯 الخلاصة

**GHOSTHAWK v2.0** جاهز الآن للاستخدام على Linux!

### أوامر التشغيل السريعة:

```bash
# عرض المساعدة
./ghosthawk.sh --help

# مسح بسيط
./ghosthawk.sh -t https://example.com

# مع Tor Proxy
./ghosthawk.sh -t https://cetj.edu.ly -p tor -T 15

# تقرير مخصص
./ghosthawk.sh -t https://example.com -o report.json -q
```

---

## 📜 الرخصة

هذا المشروع مفتوح المصدر ومتاح للأغراض التعليمية.

---

**🦅 GHOSTHAWK v2.0 - Ready for Linux! 🚀**