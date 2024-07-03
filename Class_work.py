
# def double(x):
#     print(x*2)
# LGA= ["Ilorin west", "Ekiti", "Oke-ero", "Ifelodun", "Baruteen", "Asa", "Ilorin south", "Kaima", "Saare"]
# # # # # #loop thru the array, print all the lg at the even position
# length= len(LGA)
# # # # print(length)
# for i in range(1,length,2):
#        print(LGA[i])
# # for i in range(length):
#      if (i+1)% 2 == 0:
#         print(LGA[i])
#with the help of the range function, print the ones at the odd position
# for i in range(0,length,2):
#     print(LG_in_Kwara[i])
# for i in range(length):
#     if (i+2) % 2 == 1: 
        #  print(LGA[i])
# for i in range(length):
#     print(LGA[i])
# for i in range(length):
#     if (i+2) % 2 ==1:
#         print(LGA[i])
# 
# for i in range(length):
#     print(LGA[i])
# LGAs= ["Ilorin west", "Ekiti", "Oke-ero", "Ifelodun", "Baruteen", "Asa", "Ilorin south", "Kaima", "Saare"]
# length=len(LGAs)

# vowel= "AEIOUaeiou"
# # for i in range(length):
# #      if LGAs[i][0] in vowel:
# #          print(LGAs[i])

# for lg in LGAs:
#      if lg[0] in vowel:
#           print(lg)
# # #Assignment
# #go to w3 schools, check everything on list, also, under loop, do the practice, read on functions and classes

# # double(5)
# # double(100)
# # double(8)
# # double
# numbers=[1,2,3,4]
# numbers.pop(1)


#Assignment 1
#Add LG to the end of each parameter in the list "LGAS"
#solution
#create an emptylist
# modify_LGAS= []
# #loop through the list using a for loop
# for i in LGAs:
# #append "LG" to the new list using the formular below
#     modify_LGAS.append(i + " LG")
# print(modify_LGAS)

# Assignment 2
#while loop
#for while loop, a condition must be set, and as long as that condition is True, it will continue to loop 
#through it untill the condition is no longer met.
# x=1
# while x< 6:
#     print("x is currently", x)
#     print("x is still less than 6")
#     x+=1

#create a function  that can take a number raising the function to a power of 2
# def power2(x):
#        print(x**2)# parameter is a placeholder
# power2(5)# what I am passing when calling a function is called an arguement
# power2(10)
#optional parameter- setting a default value
# def greeting(name):
#        print("good morning", name)
#        print("good morning " + name)
# def greeting(name):
#     print(f"goodmorning, {name}")
# greeting("tosin")
# greeting("Hajarat")
# def greeting(country, name="user"):
    #    print("good morning", + name,"))
#using the f-string
# def greeting(country, name="user"):
#        print(f"good morning {name}, how is {country}")
# greeting("USA", "Hajarat")
# define a function with two argument, one number and the other index
# def raise_power(x, y):
#        print(x**y)
# raise_power(5,3)
# def power(num, index):
#        print(num**index)
# var1 =5
# var2= 3
# power(var1,var2)
#define a function that will calculate the tax rate on a goods,
#  that will print 3 and 5,
#  every item in a list (number, index) adding s to the front
# def purchase(num_list):
#        for i in num_list:
#               print(i)
# purchase([1,2,3,4,5,6])
# def purchase(num_list):
#        print(num_list[4])
# def car_dealer(car_list):
#        for i in car_list
# purchase([2,4,5,6])
# def total_price(amount, tax_percentage):
#     total= amount+ (amount*tax_percentage/100)
#     # print(total)
#     return(total) #the return function can easily be manipulated
# total_price(1000,15)
# print(total_price(1000,15))
# #or you rename it
# ans= total_price(1000,15)
# print(ans)
# print(ans+2000)
# print(ans*0.5)
#        return price, tax *100
# tax_rate(5,8)
# # def car_dealer():
#        for i in 
# def polarization(item_list):
#     for item in item_list:
#         if item[-1]== "e" and item[-2]=="f":
#             print(item[0:-2]+"ves")
#         else:
#             print(item+"s")

# #
#     for i in item_list:
#         print(i+ "s")
# item_list= ["car", "plate", "phone", "wife", "knife"]
# polarization(item_list)

# amount= "N2000"
# #to remove the N infront of 2000, use the strip function
# amount= amount.strip("N") # strip is use to remove value at the end or at the begining of a string
# #split is use to remove unwanted value at the middle
# print(amount)
# val= int(amount)
# print(val/3)
# #for floor division, it helps to round up
# print(val/2)
# amount= "20,000"
# amount= amount.split(",")
# print(amount)
# amount= "".join(amount)
# print(amount)
# val= int(amount)
# print(val//2)
#assignment
#go to w3 school, finish everything on function, list, list method and classes
#create a class and instance of class
#function, list, and strings
#task 1
#write a function that adds its argument to the end of a list
# def my_function(country="Nigeria"):
#         pri
# def something()
#         print(i)
# def my_function(country="Nigeria")
# Task 1
# def addition(number):
#     return(number)
# addition([2])
# result= addition([2])
# print(result)
# new_addition= []
# new_addition.append(result)
# print(new_addition)
# def my_addition(new_list, var1):
#     new_list.append(var1)
#     return(new_list)
# list= ["Nigeria will be great"]
# new_list_2= "tosin"
# newly_created_list=my_addition(list,new_list_2)
# print(newly_created_list)
# my_addition("yam")
# print(my_addition)
# # re
# def food(list1, list2):
#     new_food.append(list2)
# result= 
# # def change_ist_element(incoming):
# # new_list[0]= incoming
# # # # #or 
# # def addition()
# def something(thelist, element):
#     return thelist.append(element)
# this= something("top", "I am")
# print(this)
#create a function that will take a list of numbers as strings, the input will be ["2000kg", "500kg"]. it will return the sum of
#["2000kg", "50kg", "40kg"]
# def my_addition(weight1, weight2, weight3):
#     print(weight1+weight2+weight3)
# weight1="2000kg"
# weight_2= "50kg"
# weight_3= "40kg"
# weight1= weight1.strip("kg")
# weight_2=weight_2.strip("kg")
# weight_3= weight_3.strip("kg")
# weight1=int(weight1)
# weight_2=int(weight_2)
# weight_3=int(weight_3)
# my_addition(weight1,weight_2,weight_3)

# def my_total(weights):
#     total=0
#     for weight in weights:
#        strVal= weight.strip("kg")
#        numval= int(strVal)
#        total= total+numval
#     return total
# weights= ["2000kg", "50kg", "40kg"]
# ans= my_total("weights")
# print(ans)
#create a function that will 
# def total_sum(lists):
#     total=0
#     for list in lists:
#         total=total+list
#     return total
# list= [2,4,5,6,4,8]
# ans= total_sum(list)
# print(ans)
# # to get the average,formular: total/length
# length=len(list)
# print(length)
# average= ans/length
# print(average)
#Assignment should be submitted on git hub
#

#     average= total/length


    
  
# # my_total(weight="2000kg")
# def add_weight

# Python Class
#it is use for creating data
# our_list = [2,4,8]
# my_list= [2, "good"]
# my_list.append("new")
# Var = 4
# word = "good"
# print(type(our_list))
# print(type(Var))
# print(type(word))
#Create a class of animal
# class Cars:
#     def __init__(self, colour, make, model):
#         self.colour= colour
#         self.make= make
#         self.model= model
#         print("new instance of car created")
#         car1= Cars("blue", "toyota", "camry")
#         car2= Cars
class Animal:
    def __init__(self, age, weight, height, colour):
        self.age=age
        self.height= height
        self.colour= colour
        self.weight= weight
    def describe(self):
        print(f"this is a {self.weight} {self.height} {self.age}yrs old {self.colour}")

animal1= Animal(20, "10cm", "40kg","white")
animal2= Animal(10, "5cm", "35kg", "black")
animal3= Animal(15, "25cm", "22kg", "black and white")
print(animal1.height)
print(animal2.height)

animal1.describe()

# Go to W3 schools, do everything on classes and inheritance
#and update it on github, do not copy word for word.



