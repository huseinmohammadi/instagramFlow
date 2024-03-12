from services.instagram import Instagram


class InstagramController(Instagram):

    def __init__(self, username, password):    
        self.username = username
        self.password = password

    def get_data(self):
        self.get_following('merzhak')
