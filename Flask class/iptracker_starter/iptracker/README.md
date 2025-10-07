# IP Tracker Demo (Flask + Firebase Realtime Database)

This classroom-ready project logs each visit's IP, user-agent, path, and timestamp to Firebase.
It also includes a simple teaching login (session-based), a dashboard, pruning, and a privacy page.

## ⚠️ Important
- This is for **education**. Replace the teaching login with **Firebase Authentication** for real apps.
- Respect privacy laws (consent, retention, minimization). Consider anonymizing IPs.
- Lock down your Firebase rules and prefer server-side writes with the Admin SDK (already used here).

## Setup

1. **Create a Firebase project → Realtime Database**. Copy the database URL, e.g.
   `https://<project>-default-rtdb.firebaseio.com`

2. **Create a service account key** (JSON) from Firebase Console → Project Settings → Service accounts.
   Download it locally.

3. **Set environment variables** (example on macOS/Linux):
   ```bash
   export FIREBASE_DB="https://<project>-default-rtdb.firebaseio.com"
   export GOOGLE_APPLICATION_CREDENTIALS="/absolute/path/to/service-account.json"
   export SECRET_KEY="some-long-random-string"
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run**:
   ```bash
   python app.py
   ```
   Visit `http://127.0.0.1:8080/`

## Reverse Proxy (Production)
If deploying behind a proxy (Render, Railway, Nginx, Cloudflare), the app uses `ProxyFix(x_for=1)`.
Adjust the number of trusted proxies if needed.

## Firebase Rules
Recommended for server Admin SDK writes (lock down public access):
```json
{
  "rules": {
    ".read": false,
    ".write": false
  }
}
```

## Teaching Login
- The login simply stores `session['uid'] = email`.
- Replace with Firebase Auth (ID token verification) for real authentication.

## Anonymizing IPs (optional)
Replace the stored IP with a truncated version if you prefer:
```python
def anonymize_ipv4(ip):
    parts = ip.split(".")
    return ".".join(parts[:3] + ["0"]) if len(parts) == 4 else ip
```
and store `anonymize_ipv4(get_client_ip())`.

## Troubleshooting
- Permission errors → check FIREBASE_DB URL & service account file path.
- All IPs look the same → adjust `ProxyFix` and confirm hosting proxy count.
- Empty dashboard → make a few requests to `/` to generate data.
