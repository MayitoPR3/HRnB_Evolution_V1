#!/usr/bin/python3
from model.base_model import Basemodel

class Amenities(Basemodel):
    def __init__(self, wifi, pools, user_add):
        super().__init__()
        self.wifi = wifi
        self.pools = pools
        self.user_add = user_add

    