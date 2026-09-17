class utils:
    @staticmethod
    def reversed(num):
        if type(num) is not int:
            raise TypeError("input must be an integer")
        if num < 0:
            return -int(str(num)[::-1])
        return int(str(num)[::-1])
    
    @staticmethod
    def formatter(num):
        if type(num) is not int:
            raise TypeError("input must be an integer")
        return bin(num), oct(num)