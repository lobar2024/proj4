class Password:
    def __init__(self, pwd):
        self.set_password(pwd)

    def set_password(self, pwd):
        if len(pwd) < 8:
            raise ValueError("Too short")
        self.__pwd = pwd

    def check(self, pwd):
        return self.__pwd == pwd
