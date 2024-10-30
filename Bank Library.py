from bank import BankAccount
account1= BankAccount("1")
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
        if action_list[i] != "deposit" or "withdraw" or "balance" or "leave": 
            print("Please insert one of the following actions: deposit, withdraw, balance or leave")