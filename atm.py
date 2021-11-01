class Atm(object):
    def __init__ (self,atm_cardnumber,pin_no):
        self.atm_cardnumber=atm_cardnumber
        self.pin_no=pin_no
        
    
    def CashWithdrawal(self):
        print("CASH HAS BEEN WITHDRAWED")
    def BalanceEnquiry(self):
        print("THIS IS THE BALANCE AMOUNT")

    

Card= Atm("123456789","123456")
print(Card.atm_cardnumber)
print(Card.pin_no)
Card.CashWithdrawal()
Card.BalanceEnquiry()