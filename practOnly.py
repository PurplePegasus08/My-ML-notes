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



dict1 = {'name': 'Mary', 'age': 22,
  'student':True,'Country': 'UAE'}
# # for i in dict1.keys():
    
# #     print(i,end=' ')
    
    
# b:float=45.2

# try:
#     iter_check=iter(b)
# except TypeError:
#     print('obj is not iterable')
# else:
#     print('obj is iterable')
    




from operator import itemgetter,indexOf

names = [('Ben','Jones'),('Peter','Parker'),
 ('Kelly','Isa')]

sorted_names = sorted(dict1,key=itemgetter(1))
print(sorted_names)



