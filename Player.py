class Player:
    def __init__(self, username):
        self.__username = username
        self.__level = 1
        self.__endless_highscore_e = 1
        self.__endless_highscore_m = 1
        self.__endless_highscore_h = 1
        self.__endless_highscore_hc = 1
        
    def increment_level(self):
        self.__level += 1
    
    def new_endless_highscore_on_easy(self, round_num):
        self.__endless_highscore_e = round_num
    
    def new_endless_highscore_on_medium(self, round_num):
        self.__endless_highscore_m = round_num
    
    def new_endless_highscore_on_hard(self, round_num):
        self.__endless_highscore_h = round_num
    
    def new_endless_highscore_on_hardcore(self, round_num):
        self.__endless_highscore_hc = round_num

    def get_username(self):
        return self.__username
    
    def get_level(self):
        return self.__level

    def get_endless_highscore_from_easy(self):
        return self.__endless_highscore_e
    
    def get_endless_highscore_from_medium(self):
        return self.__endless_highscore_m
    
    def get_endless_highscore_from_hard(self):
        return self.__endless_highscore_h

    def get_endless_highscore_from_hardcore(self):
        return self.__endless_highscore_hc
    