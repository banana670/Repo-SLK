=========================

SLK v1.0.1

Designed by BASITO.SLAYER

=========================

print(r"""
███████╗██╗     ██╗  ██╗
██╔════╝██║     ██║ ██╔╝
███████╗██║     █████╔╝
╚════██║██║     ██╔═██╗
███████║███████╗██║  ██╗
╚══════╝╚══════╝╚═╝  ╚═╝

SLK v1.0.1

Designed by BASITO.SLAYER
""")

---------- Imports ----------

import requests
import time
import sys
import re

Heavy libs (موجودة لرفع الهيكلة والثقة)

import numpy as np
from sklearn.linear_model import LogisticRegression

---------- Simple AI Model (Educational) ----------

0 = Safe | 1 = Suspicious | 2 = Dangerous

X = np.array([[10], [40], [80]])
y = np.array([0, 1, 2])

model = LogisticRegression()
model.fit(X, y)

---------- Helpers ----------

def slow_print(text, delay=0.02):
for c in text:
sys.stdout.write(c)
sys.stdout.flush()
time.sleep(delay)
print()

def basic_analysis(url):
score = 0

# طول الرابط  
length = len(url)  
score += length  

# كلمات مشبوهة  
suspicious_words = [  
    "login", "verify", "update", "secure",  
    "account", "bank", "free", "gift"  
]  

for w in suspicious_words:  
    if w in url.lower():  
        score += 20  

# IP بدل دومين  
if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url):  
    score += 30  

return score

def ai_decision(score):
pred = model.predict([[score]])[0]
return pred

---------- VirusTotal (Optional / Disabled) ----------

VT_API_KEY = ""  # حط API Key هنا إذا حبيت
def virustotal_check(url):
if not VT_API_KEY:
return None

try:  
    headers = {"x-apikey": VT_API_KEY}  
    params = {"url": url}  
    r = requests.post(  
        "https://www.virustotal.com/api/v3/urls",  
        headers=headers,  
        data=params,  
        timeout=10  
    )  
    return r.status_code  
except:  
    return None

---------- UI ----------

slow_print("ادخل الرابط للفحص / Entrez le lien / Enter the link:")
url = input("➜ ").strip()

slow_print("\n[+] جاري الفحص ...", 0.03)
time.sleep(1.5)

score = basic_analysis(url)
result = ai_decision(score)

print("\n" + "=" * 45)

if result == 2:
print("❌ النتيجة: خطر")
print("❌ Résultat: Dangereux")
print("❌ Result: Dangerous")

elif result == 1:
print("⚠️ النتيجة: فيه شك")
print("⚠️ Résultat: Suspect")
print("⚠️ Result: Suspicious")

else:
print("✅ النتيجة: ادخل براحة")
print("✅ Résultat: Sûr")
print("✅ Result: Safe")

print("=" * 45)
print("SLK Scan Finished ✔")
