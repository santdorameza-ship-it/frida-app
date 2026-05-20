# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of FRIDA seriously. If you believe you have found a security vulnerability, please report it to us **privately** before disclosing it publicly.

### How to report

Please **DO NOT** open public GitHub issues for security vulnerabilities. Instead:

1. Email: santdorameza+frida-security@gmail.com
2. Or open a [private security advisory](https://github.com/santdorameza-ship-it/frida-app/security/advisories/new) on GitHub
3. Provide as much detail as possible:
   - Type of vulnerability (XSS, injection, authentication bypass, etc.)
   - Affected component (web app, Supabase backend, IndexedDB, etc.)
   - Step-by-step reproduction
   - Impact assessment
   - Suggested mitigation (if any)

### What to expect

- **Acknowledgment**: within 48 hours of your report
- **Triage**: within 7 days we'll assess severity and confirm whether it's a vulnerability
- **Resolution**: critical issues patched within 14 days; lower severity within 30 days
- **Disclosure**: coordinated disclosure after the patch is deployed. We will credit you in the security advisory unless you prefer to remain anonymous.

## Scope

The following are **in scope** for security reports:

- The single-file `index.html` web application
- Supabase backend interaction (RLS policies, schema, exposed endpoints)
- IndexedDB local storage (data exfiltration, injection)
- QR Mesh Sync (payload tampering, injection via scanned QR)
- Service Worker (cache poisoning, offline data tampering)
- Privacy features (Conflict Mode, location fuzzing, anonymous fingerprint)

The following are **out of scope**:

- Issues only reproducible by users with physical device access
- Self-XSS or social engineering attacks against the user
- DoS via flooding (handled by Supabase ratelimit + our 5/hour app limit)
- Vulnerabilities in third-party services beyond our integration (Supabase platform, OpenStreetMap, CartoDB, cdnjs)

## Known limitations (TRL 4-5 demo state)

FRIDA is currently a working prototype validated in lab. The following are **known limitations** that will be addressed before production deployment:

1. **No authentication**: anyone can submit reports without identity verification. Anti-spam is via fingerprint + ratelimit + reputation, not auth.
2. **Photo verification is simulated**: real LLM/CV validation (YOLOv8 + Claude Vision API) is in production roadmap.
3. **Supabase anon key is public**: the `frida_reports` and `frida_events` tables are world-readable via Row Level Security. Production will move to JWT-authenticated writes.
4. **No end-to-end encryption**: report payloads are plaintext at rest. Production will add E2E encryption for sensitive fields (location in conflict zones).

## Threat Model

FRIDA defends against:

- **Spam/flooding**: 5 reports/hour per device fingerprint
- **Fake photos**: AI verification (simulated in demo, real in production)
- **Vote manipulation**: 3+ independent confirmations needed for "attended" status; max 5 actions per observer
- **Bridge tampering**: relayer cannot modify report content, only relay it
- **Location spoofing in lock mode**: when GPS is unavailable, map is locked to prevent false signals

FRIDA does **NOT** defend against:

- Coordinated multi-device attacks (will require auth in production)
- Compromised devices already running the app
- Network-level censorship or interception (use Conflict Mode for partial mitigation)

## Privacy

Per UNDP Q&A #15:
- No PII (names, emails, phone numbers) is collected by default
- Device fingerprint is SHA-256 hashed with random salt; cannot be reversed
- Conflict Mode fuzzes location to 500m radius and disables photos
- All data export complies with Apache 2.0 license terms

## Acknowledgments

This security policy follows [GitHub's Coordinated Disclosure Best Practices](https://docs.github.com/en/code-security/security-advisories) and adapts portions of [Mozilla's security guidance](https://www.mozilla.org/en-US/security/).

---

Last updated: May 2026
