#!/usr/bin/python3
# DATA TYPE Examples


########## DICTIONARY #################

cust_name =    input("Customer name: ")
cust_address = input("      Address: ")
cust_city =    input("         City: ")
cust_state =   input("        State: ")
cust_zip =     input("          Zip: ")
print(cust_name)
print(cust_address)
items = {"plates" : 3, "cups" : 1, "glasses" : 2}
for x in items:
      print(x, items[x])
no_plates =  input("Number of  Plates: ")
no_cups =    input("Number of    Cups: ")
no_glasses = input("Number of Glasses: ")
total_plates =  int(no_plates) * int(items["plates"])
total_cups =    int(no_cups) * int(items["cups"])
total_glasses = int(no_glasses) * int(items["glasses"])
total_charge = int(total_plates) + int(total_cups) + int(total_glasses)
print(cust_name)
print(cust_address)
print(cust_city)
print(cust_zip)

print(total_charge)
myplates = "You Bought {} number of plates at {} = {} dollars."
print(myplates.format(no_plates, items["plates"], total_plates))
mycups = "               {} number of cups at {} = {} dollars."
print(mycups.format(no_cups, items["cups"], total_cups))
myglasses = "         {} number of glasses at {} = {} dollars."
print(myglasses.format(no_glasses, items["glasses"], total_glasses))
mytotal = "                   Total Amount Due = {} dollars."
print(mytotal.format(total_charge))