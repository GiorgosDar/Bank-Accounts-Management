from tkinter import *
from BankAccount import *

class UsersGui:
    def init(self,App):
        self.App=App


        global root,allClients
        allClients=App.getAllCLients()
        root = Tk()

        label = Label(root, text="Welcome to our Bank", fg="white", bg="black", font=('Arial', 18))
        label.pack(padx=75, pady=75)
        loadClients()

        CreateAccountButton = Button(root, text="Create New account", command=createAccount)
        CreateAccountButton.pack(pady=20)
        CreateAccountButton.config(font=(150))

        root.title("Bank Management System")
        root.geometry("500x500")
        root.mainloop()

def loadClients():
    global clientListBox
    clientListBox = Listbox (root)
    clientListBox.pack()

    for i,client in enumerate(allClients):
        clientListBox.insert(i,client.lastName)


def createAccount():
    selectedClient=clientListBox.get(ANCHOR)
    function = lambda selectClient: [client for client in allClients if client.lastName == selectedClient][-1]
    currentClient=function(selectedClient)
    account_to_add = input("Give an account")
    balance=int(input("Give a balance"))
    currentAccount=bankaccount(account_to_add,balance)

    currentClient.addAccount(currentAccount)
    print(len(currentClient.accounts))