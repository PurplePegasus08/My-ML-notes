##functions

#def add(a,b):
    #print(a+b)
    ##return a+b


# L1: list = [1,2,3,4]
# L2: list = [5,6,7,8]


# print(L1.__add__ (L2))




# def add():
#     a = int(input("enter a number"))
#     b = int(input("enter a number"))
#     print(a+b)
    
# add()

# def add2(a,b):
#     c = a+b
#     return c

# print(add2)



# for i in range(1,9):
#     for j in range(1,9):
#         if j<=i:

#             print('*',end=' ')
#         else:
#             print(" ",end=' ')
            
#     print()
    
    
# for i in range(1,9):
#     for j in range(1,9):
#         if j>=i:

#             print('*',end=' ')
#         else:
#             print(" ",end=' ')
            
#     print()




#Function of printing table of given number
# def table():
#     num = int(input("enter a number"))

#     for i in range(1,11):
#         print(f"{num}*{i} = {num*i}")
        
# table()


#write a program that greet person with S name
# def helS():
#     l1 = ['name','sam','sampoo','nura','anurag','shark']

#     for i in l1:
#         if i.startswith('s'):
#             print(f"hello {i}")



'''dict1 = {'name': 'Mary', 'age': 22,
  'student':True,'Country': 'UAE'}'''
  
# # for i in dict1.keys():
    
# #     print(i,end=' ')
    
    
# b:float=45.2

# try:
#     iter_check=iter(b)
# except TypeError:
#     print('obj is not iterable')
# else:
#     print('obj is iterable')
    




'''from operator import itemgetter,indexOf

names = [('Ben','Jones'),('Peter','Parker'),
 ('Kelly','Isa')]

sorted_names = sorted(dict1,key=itemgetter(1))
print(sorted_names)'''

#--------------------------------------------------------------
## Atm machine code with OOPs

'''
class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
              How can I help you?
              1. Press 1 to create pin
              2. Press 2 to change pin
              3. Press 3 to check balance
              4. Press 4 to withdraw balance
              5. Something else to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else: 
            exit()
            
    def create_pin(self):
        user_pin = int(input('Enter your pin')) 
        self.pin = user_pin
        user_balance = int(input('Enter your Balance'))
        self.balance = user_balance
        
        print('pin created successfully')
        self.menu()
    
    def change_pin(self):
        old_pin = int(input('enter your old pin'))
        if old_pin == self.pin:
            newpin = int(input('Enter your new Pin'))
            self.pin = newpin
            print('Pin changed succe---lly')
        else:
            print('incorrect pin entered')
            
        self.menu()
        
    def check_balance(self):
      user_pin = int(input('Enter the pin'))
      if user_pin == self.pin:
        print('your current balance',self.balance)
        
      else:
        print('you entered wrong pin')
      self.menu()
    
    def withdraw(self):
      user_pin = int(input('Enter the pin'))
      if user_pin == self.pin:
        amount = int(input('enter the amount'))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print('withdraw succe---',self.balance)
        
      else:
        print('wrong pin entered')
    
      self.menu()
        
      
    
        
  
  
obj = Atm()
obj ###
'''

### to call attribute we don't need () and to call methods we need () like np.shape and np.info()

'''
def is_even(num):
    if num %2 ==0:
         return 'even'
    else:
        return 'odd'
        
x = is_even(4)
print(x)

'''


'''
Parameters -> Definition: Parameters are variables defined in a function's declaration. They act as placeholders for values that the function needs to operate.
Example: In def add(x, y):, x and y are parameters.
Arguments -> Definition: Arguments are the actual values you pass to a function when you call it. These values replace the parameters within the function's code.
Example: When calling add(5, 3), 5 and 3 are arguments.

'''

#def power(a=1,b=1): ## Default arguments
#    return a**b

#print(power(2,3)) ## Positional arguments

#print(power(b=2,a=3)) ## Keyword arguments


''' Python Arbitrary Arguments –
As the name suggests, sometimes the programmer does not know the number of arguments to be passed into the function.
In such cases, Python arbitrary arguments are used. In this, we use the asterisk (*) to denote this method before the parameter in the function. 
This is also called as Python *args.

Python *args allows a function to accept any number of positional arguments i.e. arguments which are non-keyword arguments, variable-length argument list.


'''

''' Variable-Length Keyword Arguments (**kwargs)
Definition: **kwargs allows a function to accept any number of keyword arguments as a dictionary.


'''


'''
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(5, 10))    # Output: 15

'''


def pro(*num):
  num = 1
  for i in num:
      num = num *i
      
  print(num)

print(pro(4,2))