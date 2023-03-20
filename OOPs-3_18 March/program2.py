'''
class Account:
    def __init__(self,acc_type,bal,min_bal):
        self.__acc_type=acc_type
        self.__bal=bal
        self.__min_bal=min_bal
        print(self.__bal)
    def get_acctype(self):
        return self.__acc_type
    def get_bal(self):
        return self.__bal
    def get_minbal(self):
        return self.__minbal
    def set_bal(self,bal):
        self.__bal = bal
    def check_min(self):
        if self.__bal > self.__min_bal:
            return False
        else:
            return True


class Customer(Account):
    def __init__(self,c_id,c_name,c_age,c_acc):
        self.__c_id=c_id
        self.__c_name=c_name
        self.__c_age=c_age
        self.__c_acc=c_acc
        
    def withdraw(self,amt):
        if(amt<=self.__bal):
            self.__bal-=amt
            print("Transaction Processing")
            return self.__bal
        elif(self.check_min()):
            raise LimitReached("Limited Exception")
            return 0
        else:
            raise OverDrawException("Overdrawn")
            return 0
        #

    def take_card(self):
        print("Take out card from the ATM")
    def get_id(self):
        return self.__c_id
    def get_name(self):
        return self.__c_name
    def get_age(self):
        return self.__c_age
    def get_acc(self):
        return self.__c_acc


class PriveledgeCustomers(Account):
    
    def __init__(self,c_id,c_name,c_age,c_acc):
        self.__c_id=c_id
        self.__c_name=c_name
        self.__c_age=c_age
        self.__c_acc=c_acc
        self.s__bp=None
        
        
           
    def get_bp(self):
        return self.__bp
        
    def inc_b(self):
        if(self.__bal>1000):
            self.__bp+=10
        else:
            self.__bp+=2

a=Account('Savings',1000,200)

p=PriveledgeCustomers(101,"Fraz",13,32)

p.inc_b()
print(p.get_bp())
print(a.get_bal())
'''

class OverDraw(Exception):
    pass
class LimitReached(Exception):
    pass
class Customer:
    def __init__(self,cid,cname,age,account):
        self.cid=cid
        self.cname=cname
        self.age=age
        self.account=account
    def withdraw(self,amount):
        try:
            if(amount>obj2.get_balance()):
                raise OverDraw
        except OverDraw:
            print("OverDraw")
            self.take_card()
            exit()
        obj2.set_balance(obj2.get_balance()-amount)
    def take_card(self):
        print("Take card out of the ATM")

    def get_customer_id(self):
        return self.cid
    def set_customer_id(self,new_id):
        self.cid=new_id
    def get_customer_name(self):
        return self.cname
    def set_customer_name(self,new_name):
        self.cname=new_name
    def get_age(self):
        return self.age
    def set_age(self,new_age):
        self.age=new_age
    def get_account(self):
        return self.account
    def set_age(self,new_account):
        self.account=new_account

class Acount:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type=account_type
        self.__balance=balance
        self.__min_balance=min_balance
    def get_account_type(self):
        return self.__account_type
    def get_balance(self):
        return self.__balance
    def get_min_balance(self):
        return self.__min_balance
    def set_balance(self,new_balance):
        self.__balance=new_balance

class PrivilegedCustomer(Customer):
    def __init__(self,cid,cname,age,account,bonus_points):
        self.cid=cid
        self.cname=cname
        self.age=age
        self.account=account
        self.__bonus_points=bonus_points

    def withdraw(self,amount):
        super().withdraw(amount)
        self.__increase_bonus()
    def get_bonus_points(self):
        return self.__bonus_points
    def __increase_bonus(self):
        if(obj2.get_balance()>1000):
            self.__bonus_points+=10
        else:
            self.__bonus_points+=2
obj1=PrivilegedCustomer(100,"Gopal",43,100,100)
obj2=Acount("Savings",1000,500)
amount1=int(input("Enter the value to be withdrawn"))
obj1.withdraw(amount1)
print("Customer balance:",obj2.get_balance())
print("Bonus points:",obj1.get_bonus_points())
try:
    if(obj2.get_balance()<obj2.get_min_balance()):
        raise LimitReached
except LimitReached:
    print("Limit Reached")
    obj1.take_card()
    exit()
obj1.take_card()


            
        
        
    









        
    


    
