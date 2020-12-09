class Highscore:
    def __init__(self):
        self.__fp_name = 'Unclaimed'
        self.__fp_round = '1'
        self.__sp_name = 'Unclaimed'
        self.__sp_round = '1'
        self.__tp_name = 'Unclaimed'
        self.__sp_round = '1'
    
    def new_fp(self, username, round_num):
        self.__fp_name = username
        self.__fp_round = round_num
    
    def new_sp(self, username, round_num):
        self.__sp_name = username
        self.__sp_round = round_num
    
    def new_tp(self, username, round_num):
        self.__tp_name = username
        self.__tp_round = round_num

    def get_fp_name(self):
        return self.__fp_name
    
    def get_fp_round(self):
        return self.__fp_round
    
    def get_sp_name(self):
        return self.__sp_name
    
    def get_sp_round(self):
        return self.__sp_round
    
    def get_tp_name(self):
        return self.__tp_name
    
    def get_tp_round(self):
        return self.__tp_round
        