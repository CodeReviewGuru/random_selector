import random as rd
from typing import TextIO

new_email_list = []
random_email_list = []

# open text file with email addresses and save them in a list. Remove the \n from the end of the list and save the result
# to a new list
with open('emailaddresses.txt', 'r') as file:
    email_address_list = file.readlines()

    for address in email_address_list:
        new_email_list.append(address.replace("\n", ""))


# Create a new file and randomly add email addresses to it
rd_address: TextIO
with open("random_addresses.txt", 'w') as rd_address:
    # replace 'x' with whatever number you how many ever addresses you need
    for number in range(x):
        rd_address.write(str(rd.choice(new_email_list) + '\n'))
