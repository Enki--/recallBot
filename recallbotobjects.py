import json


class Member(object):
    def __init__(self, name, realName='N/A', number='N/A', boss='N/A',
                 server='N/A'):
        self.name = name
        self.realName = realName
        self.number = number
        self.boss = boss
        self.server = server

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def realName(self):
        return self.__realName

    @realName.setter
    def realName(self, realName):
        self.__realName = realName

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        self.__boss = boss

    @property
    def server(self):
        return self.__server

    @server.setter
    def server(self, server):
        self.__server = server

    def toJSON(self):  # this don't work, need to fix later
        JSONdic = {'Name': self.__name,
                   'realName': self.__realName,
                   'number': self.__number,
                   'boss': self.__boss,
                   'server': self.__server
                   }
        return JSONdic


if __name__ == "__main__":
    print('This is a class, dont run this')
