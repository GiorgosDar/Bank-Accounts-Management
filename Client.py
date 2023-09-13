class Client:
    def __init__(self,firstname,lastname,afm):
        self.firstname=firstname
        self.lastname=lastname
        self.afm=afm
        self.Bank_Accounts=[]


    def addAccount(self, account):
    self.Bank_Accounts.append(account)
    account.user = self