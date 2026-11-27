# 🦅 GHOSTHAWK v2.0 - Quick Start Guide for Linux

## 🚀 البدء السريع (3 خطوات فقط!)

### الخطوة 1: تثبيت المكتبات
```bash
cd /path/to/ghosthawk-v2
pip3 install -r requirements.txt
```

### الخطوة 2: جعل السكريبت قابل للتنفيذ
```bash
chmod +x ghosthawk.sh
chmod +x cetj_security_scan_v2_linux.py
```

### الخطوة 3: التشغيل!
```bash
./ghosthawk.sh --target https://example.com
```

---

## 📋 أوامر سريعة شائعة

### عرض المساعدة:
```bash
./ghosthawk.sh --help
```

### مسح بسيط:
```bash
./ghosthawk.sh -t https://cetj.edu.ly
```

### مع Tor Proxy:
```bash
./ghosthawk.sh -t https://cetj.edu.ly -p tor -T 15
```

### تقرير مخصص:
```bash
./ghosthawk.sh -t https://example.com -o report.json
```

### وضع الصمت:
```bash
./ghosthawk.sh -t https://example.com -q
```

---

## 🔧 حل المشاكل الشائعة

### المشكلة 1: خطأ CRLF
```bash
sed -i 's/\r$//' ghosthawk.sh
sed -i 's/\r$//' cetj_security_scan_v2_linux.py
```

### المشكلة 2: مكتبات غير مثبتة
```bash
pip3 install requests beautifulsoup4
```

### المشكلة 3: Python3 غير موجود
```bash
sudo apt update && sudo apt install python3 python3-pip
```

---

## 📊 النتائج المتوقعة

عند التشغيل ستحصل على:
1. ✅ **مسح شامل** للموقع المستهدف
2. ✅ **تقرير JSON** في الملف المحدد (أو `full_security_report.json`)
3. ✅ **تحذيرات** عن الثغرات المكتشفة
4. ✅ **إحصائيات** عن حالة الموقع الأمني

---

## 📁 الملفات الناتجة

```
full_security_report.json          # التقرير الكامل
```

التقرير يحتوي على:
- Infrastructure Scan (DNS, SSL, HTTP Methods)
- Vulnerability Scan (Headers, CSRF, Mixed Content)
- SQL Injection Detection
- XSS Detection
- API Endpoint Discovery
- Cookie Security Analysis
- Rate Limiting Detection
- User Enumeration Detection
- Sensitive Files Scan

---

## 🎯 الخلاصة

**GHOSTHAWK v2.0 جاهز للاستخدام!**

```bash
./ghosthawk.sh --help  # لعرض جميع الأوامر
```

---

**🦅 GHOSTHAWK v2.0 - Ready! 🚀**