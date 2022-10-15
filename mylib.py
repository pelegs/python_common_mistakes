from collections import UserString

def func(n):
    return 2*n

class xstr(UserString):
    def len(self):
        return len(self.split())

if __name__ == "__main__":
    print('this text is from inside mylib!')
# print('this text is from inside mylib!')
