
from class_file import content
import os
filename=input('Enter content file name:') #ask for content file
#checking if file exist if not ask for file name again  
while not(os.path.exists(filename)):
    print("File does not exist.")
    filename=input('Enter content file name:')
#create object
user=content(filename)
#infinity loop break by variable 'cont'
cont=True
while cont:
    #choose the operation 
    num_op=input('''
    what you want to 
    1:view content
    2:create a new content
    3:delete content
    4:modify content
    Enter the number operation:''')
    if num_op=='1':
        user.view_content()
    elif num_op=='2':
        user.create_content()
    elif num_op=='3':
        user.del_content()
    elif num_op=='4':
        user.modify_content()
    
    exit_program=input('Do you want to do another operation[y/n]? ')
    if exit_program=='y':
        continue
    else: cont=False    
         


            

