class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Current Balance is:")
        print("10,000")

    def withdrawl1(self,curr):
        new_amount = 100 - curr
        print("You have withdrawn amount "+str(curr) + ". Your remaining balance is "+ str(new_amount))    


def main():
    Account = input("Please enter your acount image or number: ")
    Card_number = input("Insert your key number:- ")
    pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        curr = int(input("Enter the amount:- "))
        new_user.withdrawl1(curr)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()