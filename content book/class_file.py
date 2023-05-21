import pandas as pd
import datetime
import re
import test
class content:
    def __init__(self,filename):
        self.filename=filename
        # Read CSV file into a DataFrame
        data_df = pd.read_csv(filename)
        # Convert DataFrame to dictionary
        self.data_dict = data_df.to_dict(orient="list")
        

    
    
    def view_content(self):
        #view data in form of dataframe
        df=pd.DataFrame(self.data_dict)
        while True:
            num=input('''
                what you sort by
                1:Name
                2:create time
                Enter the number operation:''')
            if num=='1':
                print(df.sort_values('name'))
                break
            elif num=='2':
                print(df.sort_values('create_date'))
                break
            else:
                print('wrong number')        
        

    def create_content(self):
        print('creating a new content:')
        #take user inputs
        name=input('Enter a content name:')
        #check the name and ask for correct name
        name=test.name_check(name)
        email=input('Enter a content email:')
        #check the email address format and ask for correct email
        email=test.email_check(email)
        phone=input('Enter a content phone number:')
        #check for phone number and ask for correct phone number 
        phone=test.phone_number_check(phone)
        address=input('Enter a content address:')
        #input the entered data in dictionary
        self.data_dict['name'].append(name)
        self.data_dict['email'].append(email)
        self.data_dict['phone'].append(phone)
        self.data_dict['address'].append(address)
        self.data_dict['create_date'].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        data_df = pd.DataFrame(self.data_dict)
        data_df.to_csv(self.filename, index=False)

    def del_content(self):
        print('deleting a content')
        name=input('Enter the name of content you want to delete:')
        try :
            #locate date in dictionary by index in the name list
            index=self.data_dict['name'].index(name)
        except:
            print('the name is not in the list of content')
        else:
            #remove the element in index
            self.data_dict['name'].pop(index)
            self.data_dict['email'].pop(index)
            self.data_dict['phone'].pop(index)
            self.data_dict['address'].pop(index)
            self.data_dict['create_date'].pop(index)
            print('the content deleted sucessfully')
            #save changes to the file by Convert dictionary to DataFrame then save DataFrame to csv file
            data_df = pd.DataFrame(self.data_dict)
            data_df.to_csv(self.filename, index=False)
        

    def modify_content(self):
        print('modify a content')
        name=input('Enter the name of content you want to modify:')
     
        try :
            #locate date in dictionary by index in the name list
            index=self.data_dict['name'].index(name)
        except:
            print('the name is not in the list of content')
        else:
            #choose the operation 
            num=input('''
            what you want to change 
            1:Name
            2:email
            3:phone number
            4:address
            Enter the number operation:''')
            change_value=input('Enter the value to change it to:')    
            if num=='1':
                #check the name and ask for correct name then modify the value
                change_value=test.name_check(change_value)
                self.data_dict['name'][index]=change_value
            elif num=='2':
                #check the email address format and ask for correct email then modify the value
                change_value=test.email_check(change_value)
                self.data_dict['email'][index]=change_value
            elif num=='3':
                #check for phone number and ask for correct phone number then modify the value
                change_value=test.phone_number_check(change_value)
                self.data_dict['phone'][index]=change_value
            elif num=='4':
                self.data_dict['address'][index]=change_value
            else:
                print('wrong number')
        #save changes to the file by Convert dictionary to DataFrame then save DataFrame to csv file        
        data_df = pd.DataFrame(self.data_dict)
        data_df.to_csv(self.filename, index=False)    

 






    