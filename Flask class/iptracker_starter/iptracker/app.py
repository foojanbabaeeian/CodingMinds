# app.py
import os, time
from flask import Flask, request, render_template, session, redirect, url_for, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

# --- Flask setup ---
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-change-me")
# Trust exactly one reverse proxy (adjust x_for if you have more)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# --- Firebase Admin SDK ---
FIREBASE_DB = os.environ.get("FIREBASE_DB", "").rstrip("/")
if not FIREBASE_DB:
    raise RuntimeError("Missing FIREBASE_DB env var (e.g., https://<project>-default-rtdb.firebaseio.com)")

# Service account credentials file path
GOOGLE_CREDS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
if not GOOGLE_CREDS or not os.path.exists(GOOGLE_CREDS):
    raise RuntimeError("Missing GOOGLE_APPLICATION_CREDENTIALS or file not found. See README.md.")

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(GOOGLE_CREDS)
firebase_admin.initialize_app(cred, {"databaseURL": FIREBASE_DB})

# --- Helpers ---
def get_client_ip():
    # Prefer Cloudflare header only if present (and you are actually behind Cloudflare)
    cf = request.headers.get("CF-Connecting-IP")
    if cf:
        return cf
    # access_route respects ProxyFix (X-Forwarded-For chain). First is the client IP.
    if request.access_route:
        return request.access_route[0]
    return request.remote_addr

def push_visit(v: dict) -> str:
    ref = db.reference("/visits")
    key = ref.push(v).key
    return key

def recent_visits(limit=200):
    data = db.reference("/visits").get() or {}
    rows = [{**v, "id": k} for k, v in data.items()]
    rows.sort(key=lambda r: r.get("ts", 0), reverse=True)
    return rows[:limit]

def prune_old(days=30):
    cutoff = int(time.time()) - days*86400
    ref = db.reference("/visits")
    data = ref.get() or {}
    deleted = 0
    for k, v in data.items():
        if v.get("ts", 0) < cutoff:
            ref.child(k).delete()
            deleted += 1
    return deleted

# --- Routes ---
@app.route("/")
def index():
    v = {
        "ip": get_client_ip(),
        "ua": request.headers.get("User-Agent", ""),
        "path": request.path,
        "ts": int(time.time()),
        "uid": session.get("uid")
    }
    try:
        push_visit(v)
    except Exception as e:
        # Don't break the user page because logging failed; just note it.
        print("Visit log failed:", e)
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        # Teaching-only: set uid from email to demonstrate sessions.
        # In production, replace with Firebase Auth token verification.
        email = request.form.get("email","").strip()
        if not email:
            return render_template("login.html", error="Email required")
        session["uid"] = email.lower()
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    if not session.get("uid"):
        return redirect(url_for("login"))
    visits = recent_visits()
    return render_template("dashboard.html", visits=visits)

@app.route("/my/visits/delete", methods=["POST"])
def delete_my_visits():
    uid = session.get("uid")
    if not uid:
        return "Unauthorized", 401
    ref = db.reference("/visits")
    data = ref.get() or {}
    deleted = 0
    for k, v in list(data.items()):
        if v.get("uid") == uid:
            ref.child(k).delete()
            deleted += 1
    return redirect(url_for("dashboard"))

@app.route("/admin/prune", methods=["POST"])
def admin_prune():
    if not session.get("uid"):
        return "Unauthorized", 401
    try:
        days = int(request.form.get("days", 30))
    except ValueError:
        days = 30
    deleted = prune_old(days=days)
    return jsonify({"deleted": deleted})

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
