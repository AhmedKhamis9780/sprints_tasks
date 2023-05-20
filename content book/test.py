#check value 
import re
def email_check(email):
    #regular expression to check email address format 
    pattern = r'^([\da-zA-z][-_.]{0,1})+@(?<![-_.]@)[\da-zA-Z]([-]{0,1}[\da-zA-Z])*(\.[a-z]{2,})+$'
    #infinte loop until enter correct value
    while not(re.match(pattern, email)):
        print('wrong email address format')
        email=input('input a correct email address: ')
    return email
def name_check(name):
    #regular expression to check name is begain with captail letter and can two word
    pattern = r'^[A-Z][a-z]{1,}(\s[A-Z][a-z]{1,})*'
    #infinte loop until enter correct value
    while not(re.match(pattern, name)) :
        print('The name is not correct it must begain by capital letter')
        name=input('input a correct name: ')
    return name
def phone_number_check(number):
    #check it a number and infinte loop until enter correct value
    while not(number.isnumeric()) :
        print('the number is not correct')
        number=input('input a correct phone number: ')
    return number
    

 