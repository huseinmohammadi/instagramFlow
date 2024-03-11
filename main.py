import re
import requests

from datetime import datetime


link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

time = int(datetime.now().timestamp())

payload = {
    'username': '_husein.mhmdi',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:b.h.137913',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

with requests.Session() as session:
    r = session.get(link)
    csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
    r = session.post(login_url, data=payload, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    })


print(r.status_code)
print(r.url)
print(r.text)

