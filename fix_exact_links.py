import urllib.request
import ssl
import json
import subprocess

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

user = "unknownuniversem-blip"

# 1. Test live status of /math/ vs /math-workout-app/
for path in ["math", "math-workout-app", "smartbanker-ai"]:
    url = f"https://{user}.github.io/{path}/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            print(f"✅ {path}: HTTP {r.status} (ONLINE)")
    except urllib.error.HTTPError as e:
        print(f"❌ {path}: HTTP {e.code}")
    except Exception as e:
        print(f"⚠️ {path}: {e}")

