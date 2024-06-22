
# def double(x):
#     print(x*2)
LGA= ["Ilorin west", "Ekiti", "Oke-ero", "Ifelodun", "Baruteen", "Asa", "Ilorin south", "Kaima", "Saare"]
# # # # #loop thru the array, print all the lg at the even position
# length= len(LGA)
# # print(length)
# for i in range(1,length,2):
#        print(LGA[i])
# for i in range(length):
#     if (i+1)% 2 == 0:
#         print(LGA[i])
#with the help of the range function, print the ones at the odd position
# for i in range(0,length,2):
#     print(LG_in_Kwara[i])
# for i in range(length):
#     if (i+2) % 2 == 1: 
#          print(LGA[i])
# for i in range(length):
#     print(LGA[i])
# for i in range(length):
#     if (i+2) % 2 ==1:
#         print(LGA[i])
# 
# for i in range(length):
#     print(LGA[i])
LGAs= ["Ilorin west", "Ekiti", "Oke-ero", "Ifelodun", "Baruteen", "Asa", "Ilorin south", "Kaima", "Saare"]
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
#Add LG to the end of each variable in the list "LGAS"
#solution
#create an emptylist
modify_LGAS= []
#loop through the list using a for loop
for i in LGAs:
#append "LG" to the new list using the formular below
    modify_LGAS.append(i + " LG")
print(modify_LGAS)
