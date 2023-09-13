from Client import *

from bankaccount import *
from usersgui import *

class App:

    def __init__(self):
        account1 = BankAccount('GR12312389', 10000)
        account2 = BankAccount('GR12312385', 100)
        account3 = BankAccount('GR12312384', 1009)
        account4 = BankAccount('GR12312387', 102)
        account5 = BankAccount('GR12312380', 1033)
        account6 = BankAccount('GR12312381', 10444)
        account7 = BankAccount('GR126612385', 2098)
        account8 = BankAccount('GR123131125', 14545)

        client1.addAccount(account1)
        client1.addAccount(account2)
        client2.addAccount(account3)
        client2.addAccount(account4)
        client3.addAccount(account5)
        client3.addAccount(account6)
        client4.addAccount(account7)
        client4.addAccount(account8)
        self.allClients=[client1,client2,client3,client4]

        UsersGui(self)

    def getAllCLients(self):
            return self.allClients
