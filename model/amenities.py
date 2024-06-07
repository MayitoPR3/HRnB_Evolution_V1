from Basemodel import Basemodel


class Amenities(Basemodel):
    def __init__(self, wifi, pools, user_add):
        self.wifi = wifi
        self.pools = pools
        self.user_add = user_add

    