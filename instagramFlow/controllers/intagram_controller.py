from services.instagram import Instagram



class InstagramController(Instagram):

    def __init__(self, username, password):    
        self.username = username
        self.password = password
