from pyclbr import Function
import random

account=0
account2=0
name=''
mobile=0
balance=5000
deposit_am=0
withdraw_am=0
transfer_am=0

# Account Creating function
def creat_acc():
        print("----CREATE ACCOUNT----")
        global account
        global name
        global mobile
        account=random.randint(10000, 99999)
        name=input("Enter your name:          ")
        mobile=input("Enter your mobile number:")
        print("ACCOUNT CREATED")
        
# Account details  function
def acc_detail():
        print("----ACCOUNT DETAILS----")
        print("Your name  is         ",name)
        print("Your account no  is   ",account)
        print("Your mobile no  is    ",mobile)
        print("Your balance  is      ",balance)

# Money dspositing Function
def deposit():
        print("----DEPOSIT----")
        global balance
        global deposit_am
        deposit_am=int(input("Enter Amount to Deposit:     ₹"))
        balance=balance+deposit_am
        print("MONEY DEPOSITED")
        
# Money withdrawing fucntion
def withdraw():
        print("----WITHFRAW----")
        global balance
        global withdraw_am 
        withdraw_am=int(input("Enter Amount to withdraw:     ₹"))
        if balance >= withdraw_am:
            balance=balance-withdraw_am
            print("MONEY WITHDRAWED")
        else:
            print("Insufficient Balance!")  
            print("TRANSACTION FAILED!!")    
            withdraw_am=0      

# balance Query fucntion
def current_bal():
        print("----BALANCE QUERY----")
        print("Your current balance is  ₹",balance)

# Transfer Money function
def transfer():
        global balance
        global account2
        global transfer_am
        print("----TRANSFER----")
        print("Amount you want to transfer")
        transfer_am=int(input("₹"))
        if balance >= transfer_am:
            print("In which Account , account no?")
            account2=int(input(""))
            if account2 > 10000 and account2 < 99999:
              balance=balance-transfer_am  
              print("MONEY TRANSFERRED")
            else:
                print("Enter Proper Account No!")
                print("TRANSACTION FAILED!!")
                transfer_am=0 
                account2=0
        else:
            print("Insufficient Balance!")
            print("TRANSACTION FAILED!!")
            transfer_am=0 
            account2=0             

# Main menu
choice='y'
while choice =='y' or choice =='Y':
    ch=int(input(" 1: Create Account \n 2: Withdraw \n 3: Deposit \n 4: Transfer Money \n 5: Account Details \n 6: Current Balance \n"))
    if ch==1:
        creat_acc()
    elif ch==2:   
        if name == '' or mobile == 0:
            print("please create an account first")
        else:
            withdraw()
    elif ch==3:
        if name == '' or mobile == 0:
            print("please create an account first")
        else:
            deposit()
    elif ch==4:
       if name == '' or mobile == 0:
            print("please create an account first")
       else: 
            transfer()            
    elif ch==5:
        acc_detail()
    elif ch==6:
        current_bal()        
    else:
        print("wrong choice") 
    print("DO you want to continue? \n  Y for yes \n  N for no")
    choice=input("") 

# Final Receipt function
while choice!='y' or choice!="Y":
    print("---SAHI SALAMAT CO-OPERATIVE BANK---")
    if name != '':
        print("Name:              ",name)
    if account > 0:
        print("Account No:        ",account)        
    if mobile != 0:
        print("Mobile No:         ",mobile)        
    if withdraw_am > 0:
        print("Money Withdrawed   ₹",withdraw_am)
    if deposit_am > 0:
        print("Money Deposited    ₹",deposit_am) 
    if transfer_am > 0 and account2 >0:
        print("Transferred        ₹",transfer_am,"In Account No ",account2)    
    if balance > 0:
        print("Your Balance is    ₹",balance)
    print("---------- THANK YOU-------------")        
    break      

       



        


    
 

    

