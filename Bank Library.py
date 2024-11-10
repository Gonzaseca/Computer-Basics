from bank import BankAccount, savings_account
account1= BankAccount("1")
account2= savings_account("2")
action= input("What do you want to do?")
action_list=action.split()
for i in range(len(action_list)):
        if action_list[i] == "deposit" or "withdraw" or "balance" or "leave":    
            if action_list[i] == "deposit":
                account1.deposit()
                account1.get_balance()
                exit()
            if action_list[i] == "withdraw":
                account1.withdraw()
                account1.get_balance()
                exit()
            if action_list[i] == "balance":
                    account1.get_balance()
                    exit()
            if action_list[i] == "leave":
                print("Bye")
                exit()
        if action_list[i] != "deposit" or "withdraw" or "balance" or "leave"or "interest": 
            print("Please insert one of the following actions: deposit, withdraw, balance or leave")
        if action_list[i] == "interest":
             account2.deposit()
             account2.interest_rate()
             