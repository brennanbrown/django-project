# Security Policy

## Supported Versions

Currently supported versions of this project:

| Version | Supported          | Django Version | Python Version |
| ------- | ------------------ | -------------- | -------------- |
| Latest  | :white_check_mark: | 5.1.3 (LTS)    | 3.12.7         |
| < 2024  | :x:                | 3.0.3          | 3.9.0          |

## Security Updates (October 2024)

This project was recently upgraded to address multiple security vulnerabilities:

### Fixed Vulnerabilities

1. **Django 3.0.3 → 5.1.3**
   - Multiple CVEs fixed in Django core
   - SQL injection vulnerabilities patched
   - XSS vulnerabilities fixed
   - CSRF improvements

2. **Pillow 7.0.0 → 11.0.0**
   - CVE-2020-5312: Out-of-bounds read
   - CVE-2020-5313: Out-of-bounds read  
   - Multiple buffer overflow fixes
   - Image processing vulnerabilities

3. **Settings Security**
   - Removed hardcoded SECRET_KEY fallback
   - Removed hardcoded database password
   - Added environment-based DEBUG control
   - Added production security headers

### Current Security Features

- ✅ **Environment-based configuration** using `.env` files
- ✅ **No hardcoded secrets** in codebase
- ✅ **HTTPS enforcement** in production
- ✅ **Secure cookies** (CSRF, Session)
- ✅ **Security headers** (HSTS, XSS, Content-Type, etc.)
- ✅ **Latest dependencies** with security patches
- ✅ **PostgreSQL 15+ support** with modern adapter

## Reporting a Vulnerability

If you discover a security vulnerability, please do the following:

1. **DO NOT** open a public issue
2. Email the details to: [mail@brennanbrown.ca](mailto:mail@brennanbrown.ca)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

You should receive a response within 48 hours. If the issue is confirmed, we will:
- Work on a fix
- Release a security patch
- Credit you for the discovery (unless you prefer anonymity)

## Security Best Practices for Users

### Development
```bash
# Always use environment variables
cp .env.example .env
# Generate a unique SECRET_KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
# Set DEBUG=True only in development
```

### Production
```bash
# Never commit .env files
# Use strong, unique SECRET_KEY
# Set DEBUG=False
# Use HTTPS (SSL/TLS)
# Keep dependencies updated
# Use environment variables for all secrets
# Enable all security headers
```

### Database
- Use strong passwords
- Never commit credentials
- Use DATABASE_URL for production
- Enable SSL connections for remote databases
- Regular backups

### Dependencies
```bash
# Check for vulnerabilities regularly
pip list --outdated
# Update dependencies
pip install --upgrade -r requirements.txt
```

## Additional Security Resources

- [Django Security Documentation](https://docs.djangoproject.com/en/5.1/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [PostgreSQL Security](https://www.postgresql.org/docs/current/security.html)

## Security Checklist

Before deploying to production, ensure:

- [ ] `DEBUG = False`
- [ ] Unique `SECRET_KEY` set via environment variable
- [ ] `ALLOWED_HOSTS` configured properly
- [ ] All environment variables set correctly
- [ ] `.env` files not in version control
- [ ] HTTPS enabled with valid SSL certificate
- [ ] Database passwords are strong and secure
- [ ] All dependencies are up to date
- [ ] Security headers are enabled
- [ ] Regular backups configured
- [ ] Monitoring and logging in place

## Contact

For security concerns, contact: [mail@brennanbrown.ca](mailto:mail@brennanbrown.ca)

---

Last Updated: October 2024
