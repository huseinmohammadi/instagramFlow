import requests
import json
import re
from datetime import datetime


class Instagram:
    ENDPOINT = "https://www.instagram.com/"
    HEADER = {
        "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
        "x-requested-with": "XMLHttpRequest",
    }

    def __init__(self):
        self.username = None
        self.password = None

    def login(self):
        with requests.Session() as session:
            response = session.get(self.ENDPOINT + 'accounts/login/')
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", response.text)[0]
            header = {
                "referer": self.ENDPOINT + "accounts/login/",
                "x-csrftoken": csrf
            }
            header.update(self.HEADER)
            time = int(datetime.now().timestamp())
            payload = {
                'username': self.username,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{self.password}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }
            response = session.post(self.ENDPOINT + 'accounts/login/ajax/', data=payload, headers=header)
            if response.status_code != 200:
                response = None 
        return response
    
    def generate_header_by_username(self, username):
        header = {
                "referer": f"https://www.instagram.com/{username}/",
            }
        header.update(self.HEADER)
        return header

    def get_profile(self, username):
        header = self.generate_header_by_username(username)
        profile = requests.get(self.ENDPOINT + 'api/v1/users/web_profile_info/?username=' + username,
                               headers=header)
        if profile.status_code == 200:
            return json.loads(profile.text)['data']['user']
        return None
    
    def get_following(self, username):
        auth = self.login()
        if auth:
            user_data = self.get_profile(username)
            header = self.generate_header_by_username(username)
            data = requests.get(self.ENDPOINT + f'api/v1/friendships/{user_data["id"]}/following/?count={user_data["edge_follow"]["count"]}',
                                headers=header, cookies=auth.cookies)
            if data.status_code == 200:
                return json.loads(data.text)['users']
        return None
