class BankAccount:
    def __init__(self, account_no, account_name):
        self.data = {}

        accounts = {
            "account_no": account_no,
            "account_name": account_name,
            "account_balance": 0
        }

        for key, value in accounts.items():
            self.data[key] = value


class Transaction:
    def __init__(self, bank_account):
        self.bank_account = bank_account   # link to account

    def menu(self):
        while True:
            try:
                print("\n[1] DEPOSIT")
                print("[2] WITHDRAW")
                print("[3] SHOW BALANCE")
                print("[0] EXIT")

                num_selected = int(input("Enter your choice: "))

                if num_selected == 1:
                    amount = int(input("Enter deposit amount: "))
                    self.deposit(amount)

                elif num_selected == 2:
                    amount = int(input("Enter withdraw amount: "))
                    self.withdraw(amount)

                elif num_selected == 3:
                    self.show_balance()

                elif num_selected == 0:
                    print("Thank you for using our kiosk!")
                    break

            except ValueError:
                print("\nInvalid input.\n")


    def deposit(self, amount):
        self.bank_account.data["account_balance"] += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        balance = self.bank_account.data["account_balance"]


        if amount > balance:
            print("Insufficient balance.")
        else:
            self.withdraw_with_fee(amount)
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        name = self.bank_account.data["account_name"]
        bal = self.bank_account.data["account_balance"]
        print(f"\nAccount: {name}")
        print(f"Balance: {bal}")

    def withdraw_with_fee(self, amount):
        fee = 20
        total = amount + fee
        balance = self.bank_account.data["account_balance"]

        if total > balance:
            print("Not enough balance including fee.")
        else:
            self.bank_account.data["account_balance"] -= fee
            self.bank_account.data["account_balance"] -= amount




print("\n========================================")
account_name = input("Enter your account name: ")
account_no = int(input("Please input your account number: "))
print("========================================\n")

bank_account = BankAccount(account_no, account_name)
transaction = Transaction(bank_account)
transaction.menu()

