import random
details_storage={
            '0123456789':{
            'first_name':'JOHN', 
            'last_name':'DOE',
            'login_pin':'1234',
            'transaction_pin':'4321'}
            }
            
transfer_data={
            '0123456789':{
            'first_name':'JOHN', 
            'last_name':'DOE',}

            }
data={
            '0123456789':{
            'first_name':'JOHN', 
            'last_name':'DOE',
            'login_pin':'1234',
            'transaction_pin':'4321',
            'balance':'300_000.00'}
            }

        
def generate_account_number():
            account_number=random.randint(100000000,999999999)
            account_number=str( account_number)
            account_number='0'+ account_number
            return account_number
            

def set_login_pin():
            login_pin=random.randint(1000,9999)
            return login_pin
            

def set_transaction_pin():
            transaction_pin=input('Enter a 4 digit pin of your choice for transactions:')
            return transaction_pin
            
class account_holder:
        def __init__(self,first_name,last_name,login_pin,transaction_pin,account_number):
            self.first_name=first_name
            self.last_name=last_name
            self.login_pin=login_pin
            self.transaction_pin=transaction_pin
            self.account_number=account_number
            
        def check_details(self):
            z=str(self.account_number)
            x=self.first_name
            u=self.last_name
            y=str(self.login_pin)
            w=str(self.transaction_pin)
            null= {z:{
                    'first_name':x,
                    'last_name':u,
                    'login_pin':y,
                    'transaction_pin':w}}
                
           
            
            for keyz,valuez in details_storage.items():
                m={}
                m[keyz]=valuez
                
                if  m==null:
                   
                    return True
            
        def check_account_balance(self):
        
            print(data[self.account_number]['balance'])
            login()
            
        def transfer(self):
        
            amount=float(input('How much do you wish to transfer:'))
            total=float(data[self.account_number]['balance'])
            print('Who do you want to transfer to?')
            fname=input('First name:').upper()
            lname=input('Last name:').upper()
            account_num=input('Account number:')
            
            null={
                account_num:{
                    'first_name':fname,
                    'last_name':lname,
                    
                }}
            
            for keyz,valuez in transfer_data.items():
                l={}
                l[keyz]=valuez
                if l ==null:
                            if amount<total:
                                
                                final_balance=total-amount
                                print('Your new balance is:',final_balance)
                                print('You sent',amount)
                                data[self.account_number]['balance']=str(final_balance)
                                login()
                                return final_balance
                                
                        
                            else:
                                print('Insufficent Funds')
                                d=input('Do you want to try again? Yes or No:').upper()
                                if d=='YES':
                                    login()
                                elif d=='NO':
                                    h=input('Do you want to exit? Yes or No:').upper()
                                    if h=='YES':
                                        print('Exiting....')
                                        exit()
                                    elif h=='YES':
                                        login()
                                    else:
                                        print('Wrong Input')
                                        login()
                                else:
                                    print('Wrong Input')
                                    login()
                        
                        
                else :
                            print('Not a User')
                            login()
                
            
            
            
            
        
        def deposit(self):
        
            amount=float(input('How much do you wish to deposit:'))
            total=float(data[self.account_number]['balance'])
            final_balance=total+amount
            print('Your new balance is:',final_balance)
            data[self.account_number]['balance']=final_balance
            login()   
            return final_balance
            
            
        def withdraw(self):
            if amount<total:
                amount=float(input('How much do you wish to withdraw:'))
                total=float(data[self.account_number]['balance'])
                final_balance=total-amount
                print('Your new balance is:',final_balance)
                data[self.account_number]['balance']=final_balance
                login()
                return final_balance
                
            else:
                print('Insufficient Funds')
                login()
        
        
        
            
        

def login():

    print('Do you have an account?')
    answer=input('Enter Yes or No :').upper()


    if answer=='YES':

        first_name= input('Enter First name:').upper()
        last_name= input('Enter Last name:').upper()
        login_pin= input('Enter 4 digit Login Pin:')
        account_number= input('Enter Account Number:')
        transaction_pin= input('Enter Transaction Pin:')

        Holder=account_holder(first_name,last_name,login_pin,transaction_pin,account_number)
       
        h=Holder.check_details()
        
        if h == True:
            print('''How may we help you?
            Check my balance (1)
            Deposit Money (2)
            Withdraw (3)
            Transfer (4)
            Exit(5)''')
           
            action=input('Input option number :')
            
            if action=='1':
                print(Holder.check_account_balance())                   
            elif action=='2':
                
                print(Holder.deposit())
                
            elif action=='3':
                print(Holder.withdraw())
                
            elif action=='4':
                print(Holder.transfer())
            elif action=='5':
                f=input('''Do you wish to leave?
                Yes or No''').upper()
                if f=='YES':
                    exit()
                elif f=='NO':
                    login()
                else:
                    print('Wrong input')
        else:
                print('You do not have an account with us')
                login()
                
        

        
        
        
        
    elif answer=='NO':
        first_name= input('Enter First name:').upper()
        last_name= input('Enter Last name:').upper()
        x=str(generate_account_number())
        y=str(set_login_pin())
        z=str(set_transaction_pin())
        
        print(f'''{first_name} {last_name}Your New Account number is {x},
              Your Login Pin is {y},
              Your chosen Transaction pin is {z}
              You current balance is 0''')
        details_storage[x]={
                    'first_name': first_name,
                    'last_name':last_name,
                    'login_pin':y,
                    'transaction_pin':z}
        

    

        data[x]={
            
            'first_name':first_name, 
            'last_name':last_name,
            'login_pin':y,
            'transaction_pin':z,
            'balance':0
            }
                    
        transfer_data[x]={
            'first_name':first_name, 
            'last_name':last_name,

            }
        s=input('Do you want to Log in or Exit:').upper()
        if s=='LOG IN':
            login()
        elif s=='EXIT':
            print('Good Bye')
            exit()
        else:
            print('Wrong Input')
            login()
            
        
        
       
    else:
        print('Wrong Input')


login()