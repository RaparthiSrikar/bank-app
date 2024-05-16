class BankAccount:
    no_of_customers  = 0
    account_number = 34567850

    def __init__(self, name, mobile_number, initial_deposit, pin):
        self.name = name  #instant variable
        self.cust_acc_num = BankAccount.account_number
        self.mobile_number = mobile_number
        self.account_balance = initial_deposit
        self.pin = pin

        BankAccount.account_number = BankAccount.account_number + 1
        BankAccount.no_of_customers = BankAccount.no_of_customers + 1
        

    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: {self.account_balance}')
    
    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.account_balance = self.account_balance + amount
            print(f'Transaction completed. Current Balance: {self.account_balance}')
        else:
            print('Invalid amount transaction aborted')
    
    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.account_balance and amount > 0:
            self.account_balance = self.account_balance - amount
            print(f'Transaction completed. Current Blance: {self.account_balance}')
        else:
            print('Invalid amount transaction aborted')
    
    def payment(self, other):
        amount = int(input('Enter the payment amount: '))
        if amount <= self.account_balance and amount > 0:
            self.account_balance = self.account_balance - amount
            other.account_balance = other.account_balance + amount
            print(f'Transaction completed. Current Balance: {self.account_balance}')
        else:
            print('Invalid amount transaction aborted')

if __name__ == '__main__' :
    cust1 = BankAccount(name="Srikar", mobile_number=9876543210, initial_deposit=1000, pin=3567)
    cust2 = BankAccount(name="Karthik", mobile_number=9087654321, initial_deposit=2000, pin=9876)
    print('No of customers is', BankAccount.no_of_customers)
    print(cust1.basic_details())
    print(cust2.basic_details())
    cust1.deposit()
    print(cust1.basic_details())
    cust1.withdrawl()
    print(cust1.basic_details())
    cust1.payment(cust2)
    print(cust2.basic_details())