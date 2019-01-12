# A program to calculate the number of months it will take to deplete retirement
#savings.
# Alieu Sanneh
# 5/18/17

#main function
# draws the retirement table showing the starting balance, assumed interest
#rates and the number of months it will take to deplete the savings, given
#the monthly spenings provided by the user.

def main ():
     print( "Welcome to the retirement planning tool!")
     print()
     amnt_spent = float(input("Please enter monthly"\
                                  " spending ( at least $500 ):"))

     while amnt_spent < 500:
          amnt_spent = float(input("must be at least 500:"))
          #validates that the user inputs at least 500
     
     print()

     print("Retirement Savings Table:")
     print()
     print('Starting    Asummed     Interest   Rate')
     print('Balance     3%       5%     7%       9%')
     print()
     for ini_balance in range(450000, 950000, 50000):
          #the program provides details for balances ranging from
          #450000 to 900000
          
           print('$' + str(ini_balance),end=' ')

           for int_rate in range(3, 11, 2):
             print(format(calc_months(ini_balance,int_rate,amnt_spent),\
                    '7.0f'),end = ' ')
           print()

          

          
#The calc_months function returns the number of months it will take for a
#retirement savings to drop to zero or less. It uses the initial balance
#in the account, the yearly interest rate (converted to a montly rate) 
#and the monthly spendings as paramenters.
#the initial balance is reduced by the amount spent each month, and then
#increased by the interest gained for that month. This process iterates
#monthly as long as the account balance is greater than zero and the 
#number of months is less than 600.
#At the end of each month, the months counter is updated and the process
#restarts until the acount balance is <=0 or months >=600, then program returns
#the corresponding number of months.
           
def calc_months(ini_balance, int_rate, amnt_spent):
     #initial balance at retirement
     #interst rate per annum
     #amount spent per month
     #previously validated
     
     months = 0 #initializes months counter         
 
     
     while ini_balance > 0 and months in range(600):
          ini_balance -= amnt_spent
          interest = ini_balance * ((int_rate/100)/12)
          #divided by 12 to convert to monthly interest
          
          ini_balance += interest
          months +=1     #updates the months counter
          
     return months
main()

#Documentation

#Test case 1

#When the Program was tested with a monthly spending of $5000, the following
#results were produced

#Welcome to the retirement planning tool!

#Please enter monthly spending ( at least $500 ):5000

#Retirement Savings Table:

#Starting    Asummed     Interest   Rate
#Balance     3%       5%     7%       9%

#$450000     102     113     127     149 
#$500000     115     129     150     183 
#$550000     129     147     175     229 
#$600000     143     166     205     300 
#$650000     157     187     242     460 
#$700000     172     210     288     600 
#$750000     188     235     351     600 
#$800000     204     263     453     600 
#$850000     221     294     600     600 
#$900000     239     331     600     600

#Test case 2

#When the Program was tested with a monthly spending of $501, the following
#results were produced

#Retirement Savings Table:

#Starting    Asummed     Interest   Rate
#Balance     3%       5%     7%       9%

#$450000     600     600     600     600 
#$500000     600     600     600     600 
#$550000     600     600     600     600 
#$600000     600     600     600     600 
#$650000     600     600     600     600 
#$700000     600     600     600     600 
#$750000     600     600     600     600 
#$800000     600     600     600     600 
#$850000     600     600     600     600 
#$900000     600     600     600     600   

#the above test case shows that the account is growing faster that it is being
#spent.
#to avoid an imfinite loop, the program is set to stop when the number of
#months is at most 600.

#Test case 3

#When the Program was tested with a monthly spending of $30000, the following
#results were produced


#Retirement Savings Table:

#Starting    Asummed     Interest   Rate
#Balance     3%       5%     7%       9%

#$450000      16      16      16      16 
#$500000      18      18      18      18 
#$550000      19      20      20      20 
#$600000      21      21      22      22 
#$650000      23      23      24      24 
#$700000      25      25      25      26 
#$750000      26      27      27      28 
#$800000      28      29      29      30 
#$850000      30      31      31      32 
#$900000      32      32      33      34 


#Hand calculations using compound interest formula yields the same
#results as the program.
